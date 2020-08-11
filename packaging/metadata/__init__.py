import os
import re
import tarfile
import textwrap

try:
    from StringIO import StringIO  ## for Python 2
except ImportError:
    from io import StringIO  ## for Python 3
from email.parser import HeaderParser
from email import message_from_string
from email.message import Message
import json
from six import with_metaclass
from .distributions import SDistTar, SDistZip, Wheel, Distribution
from .constants import VERSIONED_METADATA_FIELDS
from .exceptions import (
    UnknownDistributionFormat,
    NoMetadataFound,
    MultipleMetadataFound,
)

distribution_types = {
    ".whl": Wheel,
    ".tar.bz2": SDistTar,
    ".tar.gz": SDistTar,
    ".zip": SDistZip,
}

try:
    UNICODE_CLASS = unicode
except NameError:
    UNICODE_CLASS = str


def json_form(val):
    return val.lower().replace("-", "_")


class Metadata:
    def __init__(self, **kwargs):
        self.meta_dict = kwargs

    def __eq__(self, other):
        if isinstance(other, Metadata):
            return self.meta_dict == other.meta_dict
        return False

    @classmethod
    def from_json(cls, data):
        return cls(**Metadata._canonicalize(json.loads(data)))

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    @classmethod
    def from_file(cls, filename, filetype=None):
        if filetype:
            if issubclass(filetype, Distribution):
                distribution = filetype(filename)
            else:
                raise UnknownDistributionFormat
        else:
            for extension, distribution_cls in distribution_types.items():
                if filename.endswith(extension):
                    distribution = distribution_cls(filename)
                    break
            else:
                raise UnknownDistributionFormat
        # print("PKG-INFO string")
        # print(distribution.extract_pkginfo())
        return cls(**Metadata._pkginfo_string_to_dict(distribution.extract_pkginfo()))

    @classmethod
    def from_rfc822(cls, pkginfo_string):
        return cls(**Metadata._pkginfo_string_to_dict(pkginfo_string))

    def to_json(self):
        return json.dumps(self.meta_dict, sort_keys=True)

    # def to_rfc822(self):
    #     msg = Message()
    #     for field in SINGLE | MULTI | TREAT_AS_MULTI:
    #         value = self.meta_dict.get(json_form(field))
    #         if value:
    #             if field == "Description":
    #                 # Special case - put in payload
    #                 msg.set_payload(value)
    #                 continue
    #             if field == "Keywords":
    #                 value = ", ".join(value)
    #             if isinstance(value, str):
    #                 value = [value]
    #             for item in value:
    #                 msg.add_header(field, item)

    #     return msg.as_string()

    def to_rfc822(self):
        msg = Message()
        for field in SINGLE | MULTI:
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
    def _pkginfo_string_to_dict(cls, string):
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
        parsed = HeaderParser().parse(StringIO(string))
        metadata_fields = VERSIONED_METADATA_FIELDS[parsed.get("Metadata-Version")]

        for key, value in parsed.items():

            if not isinstance(key, UNICODE_CLASS):
                key = key.decode("utf-8")
            if not isinstance(value, UNICODE_CLASS):
                value = value.decode("utf-8")

            if key in metadata_fields["MULTI"]:
                if key not in metadata:
                    metadata[key] = []
                metadata[key].append(value)
            elif key in metadata_fields["TREAT_AS_MULTI"]:
                metadata[key] = [val.strip() for val in value.split(",")]
            elif key == "Description":
                value = cls.standardize_description_field(value)
                metadata[key] = value
            else:
                metadata[key] = value
        payload = parsed.get_payload()
        if payload:
            if "Description" in metadata:
                print("Both Description and payload given - ignoring Description")
            metadata["Description"] = payload

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
        return {json_form(key): value for key, value in metadata.items()}

    def validate(self):
        raise NotImplementedError

    @classmethod
    def standardize_description_field(cls, description):
        description_lines = description.splitlines()

        if len(description_lines) == 1:
            return description

        first_line = description_lines[0].lstrip()
        dedented = "\n".join(
            [first_line, textwrap.dedent("\n".join(description_lines[1:]))]
        )

        return dedented
