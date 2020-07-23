import os
import re
import tarfile

from email.parser import HeaderParser
from email import message_from_string
from email.message import Message
import json
from six import with_metaclass
from . distributions import SDistTar, SDistZip, Wheel
from . constants import MULTI, SINGLE, TREAT_AS_MULTI

class UnknownDistributionFormat(Exception):
    pass


class NoMetadataFound(Exception):
    pass


class MultipleMetadataFound(Exception):
    pass



distribution_types = {
    ".whl": Wheel,
    ".tar.bz2": SDistTar,
    ".tar.gz": SDistTar,
    ".zip": SDistZip,
}

def json_form(val):
    return val.lower().replace("-", "_")

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
                distribution = distribution_cls(filename)
                break
        else:
            raise UnknownDistributionFormat

        return cls(**Metadata._metadata_from_pkginfo_string(distribution.extract_pkginfo()))
    
    @classmethod
    def from_rfc822(cls, pkginfo_string):
        return cls(**Metadata._metadata_from_pkginfo_string(pkginfo_string))

    
    def to_json(self):
        return json.dumps(self.meta_dict)

    def to_rfc822(self):
        msg = Message()
        for field in SINGLE | MULTI | TREAT_AS_MULTI:
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

    def to_dict(self):
        return self.meta_dict

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
            if key in MULTI:
                if key not in metadata:
                    metadata[key] = []
                metadata[key].append(value)
            elif key in TREAT_AS_MULTI:
                metadata[key] = [val.strip() for val in value.split(',')]
            else:
                metadata[key] = value
        
        payload = parsed.get_payload()
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
