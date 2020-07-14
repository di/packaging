import os
import re
import tarfile
from email.parser import HeaderParser
from email import message_from_string
from email.message import EmailMessage
import json
from six import with_metaclass

import constants
# from . import validators


class UnknownDistributionFormat(Exception):
    pass


class NoMetadataFound(Exception):
    pass


class MultipleMetadataFound(Exception):
    pass


class Distribution:
    def __init__(self, filename):
        self.filename = filename

    def extract_pkginfo(self):
        raise NotImplementedError


class Wheel(Distribution):
    pass


class WinInst(Distribution):
    pass


class BDist(Distribution):
    pass


class SDist(Distribution):
    pass


class SDistZip(SDist):
    pass


class SDistTar(SDist):

    def extract_pkginfo(self):
        archive = tarfile.open(self.filename)
        dirname = os.path.commonprefix(archive.getnames())
        member = archive.extractfile('/'.join([dirname, 'PKG-INFO']))
        if member:
            return member.read().decode()
        raise NoMetadataFound


distribution_types = {
    ".whl": Wheel,
    ".exe": WinInst,
    ".egg": BDist,
    ".tar.bz2": SDistTar,
    ".tar.gz": SDistTar,
    ".zip": SDistZip,
}

def json_form(val):
    return val.lower().replace("-", "_")

class Field:
    def __init__(self, validators=None):
        self.validators = validators
        self.data = None

    def validate(self):
        raise NotImplementedError(self)


class SingleField(Field):
    def validate(self):
        pass

class MultiField(Field):
    pass


class MetadataMeta(type):
    def __init__(cls, name, bases, attrs):
        type.__init__(cls, name, bases, attrs)
        cls.fields = None

    def __call__(cls, *args, **kwargs):
        if cls.fields is None:
            fields = []
            for name in dir(cls):
                if not name.startswith('_'):
                    unbound_field = getattr(cls, name)
                    if isinstance(unbound_field, Field):
                        fields.append((name, unbound_field))
            fields.sort()
            cls.fields = fields

        return type.__call__(cls, *args, **kwargs)


class BaseMetadataSpecification(with_metaclass(MetadataMeta)):

    def __init__(self, meta_dict):
        for field_name, field in self.fields:
            field.data = meta_dict.get(field_name)

    def validate(self):
        for field_name, field in self.fields:
            field.validate()

    # Metadata version
    metadata_version = SingleField(validators=[])


class Metadata1_2Specification(BaseMetadataSpecification):

    # Identity Project and Release
    name = SingleField(
        validators=[],
    )
    version = SingleField(
        validators=[],
    )

    # Additional Release metadata
    summary = SingleField(
        validators=[],
    )
    description = SingleField(
        validators=[],
    )
    author = SingleField()
    author_email = SingleField(
        validators=[],
    )
    maintainer = SingleField(
        validators=[],
    )
    maintainer_email = SingleField(
        validators=[],
    )
    license = SingleField(validators=[])
    keywords = SingleField(validators=[])
    classifiers = MultiField(validators=[])
    platform = SingleField(validators=[])

    # URLs
    home_page = SingleField(
        validators=[],
    )
    download_url = SingleField(
        validators=[],
    )

    # Dependency Information
    requires_python = SingleField(
        validators=[],
    )

    # File information
    pyversion = SingleField(
        validators=[],
    )
    filetype = SingleField(
        validators=[]
    )
    comment = SingleField(validators=[])
    md5_digest = SingleField(
        validators=[],
    )
    sha256_digest = SingleField(
        validators=[]
    )
    blake2_256_digest = SingleField(
        validators=[]
    )

    # Legacy dependency information
    requires = MultiField(
        validators=[]
    )
    provides = MultiField(
        validators=[],
    )
    obsoletes = MultiField(
        validators=[],
    )

    # Newer dependency information
    requires_dist = MultiField(
        validators=[],
    )
    provides_dist = MultiField(
        validators=[],
    )
    obsoletes_dist = MultiField(
        validators=[],
    )
    requires_external = MultiField(
        validators=[],
    )

    # Newer metadata information
    project_urls = MultiField(
        validators=[],
    )


class Metadata:

    def __init__(self, **kwargs):
        self.meta_dict = kwargs
        #self.validate()

    def __eq__(self, other):
        if isinstance(other, Metadata):
            return self.meta_dict == other.meta_dict


    @classmethod
    def from_json(cls, data):
        return cls(**Metadata._canonicalize(json.loads(data)))
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    @classmethod
    def from_file(cls, filename):
        for extension, distribution_cls in distribution_types.items():
            if filename.endswith(extension):
                self.distribution = distribution_cls(filename)
                break
        else:
            raise UnknownDistributionFormat

        return cls(**Metadata._metadata_from_pkginfo_string(self.distribution.extract_pkginfo()))
    
    @classmethod
    def from_rfc822(cls, pkginfo_string):
        return cls(**Metadata._metadata_from_pkginfo_string(pkginfo_string))

    
    def to_json(self):
        return json.dumps(self.meta_dict)

    def to_rfc822(self):
        msg = EmailMessage()
        for field in constants.SINGLE | constants.MULTI | constants.TREAT_AS_MULTI:
            value = self.meta_dict.get(json_form(field))
            if value:
                if field == "Description":
                    # Special case - put in payload
                    msg.set_payload(value)
                    continue
                if field == "Keywords":
                    value = ", ".join(value)
                if isinstance(value, str):
                    value = [value]
                for item in value:
                    msg.add_header(field, item)

        return msg.as_string()

    def __iter__(self):
        return iter(self.meta_dict.items())

    @classmethod
    def _metadata_from_pkginfo_string(cls, string):
        """Extracts metadata information from a metadata-version 2.1 object.

        https://www.python.org/dev/peps/pep-0566/#json-compatible-metadata

        - The original key-value format should be read with email.parser.HeaderParser;
        - All transformed keys should be reduced to lower case. Hyphens should
          be replaced with underscores, but otherwise should retain all other
          characters;
        - The transformed value for any field marked with "(Multiple-use")
          should be a single list containing all the original values for the
          given key;
        - The Keywords field should be converted to a list by splitting the
          original value on whitespace characters;
        - The message body, if present, should be set to the value of the
          description key.
        - The result should be stored as a string-keyed dictionary.
        """
        metadata = {}
        parsed = HeaderParser().parsestr(string)
        for key, value in parsed.items():
            if key in constants.MULTI:
                if key not in metadata:
                    metadata[key] = []
                metadata[key].append(value)
            elif key in constants.TREAT_AS_MULTI:
                metadata[key] = [val.strip() for val in value.split(',')]
            else:
                metadata[key] = value
        
        payload = message_from_string(string).get_payload()
        
        if payload:
            if "description" in metadata:
                print("Both Description and payload given - ignoring Description")
            
            metadata["description"] = payload
        
        return Metadata._canonicalize(metadata)

    @classmethod
    def _canonicalize(cls, metadata):
        """
        Transforms a metadata object to the canonical representation
        as specified in
        https://www.python.org/dev/peps/pep-0566/#json-compatible-metadata
        All transformed keys should be reduced to lower case. Hyphens
        should be replaced with underscores, but otherwise should retain all
        other characters.
        """
        return {
            json_form(key): value
            for key, value in metadata.items()
        }

    def validate(self):
        raise NotImplementedError
