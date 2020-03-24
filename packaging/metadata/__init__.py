import os
import re
import tarfile
from email.parser import HeaderParser

from . import constants
from . import validators


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

_dist_file_regexes = {
    # True/False is for legacy or not.
    True: re.compile(
        r".+?\.(exe|tar\.gz|bz2|rpm|deb|zip|tgz|egg|dmg|msi|whl)$",
        re.I,
    ),
    False: re.compile(r".+?\.(tar\.gz|zip|whl|egg)$", re.I),
}


_wheel_file_re = re.compile(
    r"""
    ^
    (?P<namever>(?P<name>.+?)(-(?P<ver>\d.+?))?)
    (
        (-(?P<build>\d.*?))?
        -(?P<pyver>.+?)
        -(?P<abi>.+?)
        -(?P<plat>.+?)
        (?:\.whl|\.dist-info)
    )
    $
    """,
    re.VERBOSE,
)


_project_name_re = re.compile(
    r"^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$",
    re.IGNORECASE,
)


_legacy_specifier_re = re.compile(
    r"^(?P<name>\S+)(?: \((?P<specifier>\S+)\))?$"
)


class Field:
    def __init__(self, validators=None):
        self.validators = validators

    def validate(self):
        raise NotImplementedError


class SingleField(Field):
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


class BaseMetadataValidator(metaclass=MetadataMeta):

    def __init__(self, meta_dict):
        self.meta_dict = meta_dict

    def validate(self):
        for field_name, validator in self.fields:
            print(field_name)

    # Metadata version
    metadata_version = SingleField(
        validators=[
            validators.Required(),
            validators.AnyOf(
                # Note: This isn't really Metadata 2.0, however bdist_wheel
                #       claims it is producing a Metadata 2.0 metadata when in
                #       reality it's more like 1.2 with some extensions.
                ["1.0", "1.1", "1.2", "2.0"],
                message="Unknown Metadata Version",
            ),
        ],
    )


class Metadata1_2Validator(BaseMetadataValidator):

    # Identity Project and Release
    name = SingleField(
        validators=[
            validators.Required(),
            validators.Regexp(
                _project_name_re,
                re.IGNORECASE,
                message=(
                    "Must start and end with a letter or numeral and contain "
                    "only ascii numeric and '.', '_' and '-'."
                ),
            ),
        ],
    )
    version = SingleField(
        validators=[
            validators.Required(),
            validators.Regexp(
                r"^(?!\s).*(?<!\s)$",
                message="Cannot have leading or trailing whitespace.",
            ),
            # _validate_pep440_version,
        ],
    )

    # Additional Release metadata
    summary = SingleField(
        validators=[
            validators.Optional(),
            validators.Length(max=512),
            validators.Regexp(
                r"^.+$",  # Rely on the fact that . doesn't match a newline.
                message="Multiple lines are not allowed.",
            )
        ],
    )
    description = SingleField(
        validators=[validators.Optional()],
    )
    author = SingleField(validators=[validators.Optional()])
    author_email = SingleField(
        validators=[
            validators.Optional(),
            validators.RFC822Email(),
        ],
    )
    maintainer = SingleField(
        validators=[validators.Optional()],
    )
    maintainer_email = SingleField(
        validators=[
            validators.Optional(),
            validators.RFC822Email(),
        ],
    )
    license = SingleField(validators=[validators.Optional()])
    keywords = SingleField(validators=[validators.Optional()])
    classifiers = MultiField(validators=[validators.AnyOf([])])
    platform = SingleField(validators=[validators.Optional()])

    # URLs
    home_page = SingleField(
        validators=[
            validators.Optional(),
            validators.URI(),
        ],
    )
    download_url = SingleField(
        validators=[
            validators.Optional(),
            validators.URI(),
        ],
    )

    # Dependency Information
    requires_python = SingleField(
        validators=[
            validators.Optional(),
            # _validate_pep440_specifier_field,
        ],
    )

    # File information
    pyversion = SingleField(
        validators=[validators.Optional()],
    )
    filetype = SingleField(
        validators=[
            validators.Required(),
            validators.AnyOf(
                [
                    "bdist_dmg", "bdist_dumb", "bdist_egg", "bdist_msi",
                    "bdist_rpm", "bdist_wheel", "bdist_wininst", "sdist",
                ],
                message="Unknown type of file.",
            ),
        ]
    )
    comment = SingleField(validators=[validators.Optional()])
    md5_digest = SingleField(
        validators=[
            validators.Optional(),
        ],
    )
    sha256_digest = SingleField(
        validators=[
            validators.Optional(),
            validators.Regexp(
                r"^[A-F0-9]{64}$",
                re.IGNORECASE,
                message="Must be a valid, hex encoded, SHA256 message digest.",
            ),
        ]
    )
    blake2_256_digest = SingleField(
        validators=[
            validators.Optional(),
            validators.Regexp(
                r"^[A-F0-9]{64}$",
                re.IGNORECASE,
                message="Must be a valid, hex encoded, blake2 message digest.",
            ),
        ]
    )

    # Legacy dependency information
    requires = MultiField(
        validators=[
            validators.Optional(),
            # _validate_legacy_non_dist_req_list,
        ]
    )
    provides = MultiField(
        validators=[
            validators.Optional(),
            # _validate_legacy_non_dist_req_list,
        ],
    )
    obsoletes = MultiField(
        validators=[
            validators.Optional(),
            # _validate_legacy_non_dist_req_list,
        ],
    )

    # Newer dependency information
    requires_dist = MultiField(
        validators=[
            validators.Optional(),
            # _validate_legacy_dist_req_list,
        ],
    )
    provides_dist = MultiField(
        validators=[
            validators.Optional(),
            # _validate_legacy_dist_req_list,
        ],
    )
    obsoletes_dist = MultiField(
        validators=[
            validators.Optional(),
            # _validate_legacy_dist_req_list,
        ],
    )
    requires_external = MultiField(
        validators=[
            validators.Optional(),
            # _validate_requires_external_list,
        ],
    )

    # Newer metadata information
    project_urls = MultiField(
        validators=[
            validators.Optional(),
            # _validate_project_url_list,
        ],
    )


class Metadata:

    def __init__(self, as_dict=None, filename=None, string=None):
        """
            as_dict - must be canonicalized dictionary
            filename - must be path to a distribution
            string - must be the contents of a pkginfo file
        """

        if as_dict:
            self.meta_dict = as_dict

        elif filename:
            for extension, distribution_cls in distribution_types.items():
                if filename.endswith(extension):
                    self.distribution = distribution_cls(filename)
                    break
            else:
                raise UnknownDistributionFormat

            self.meta_dict = self._metadata_from_pkginfo_string(
                self.distribution.extract_pkginfo()
            )

        elif string:
            self.meta_dict = self._metadata_from_pkginfo_string(string)

        else:
            raise Exception('Must provide an argument')

    def __iter__(self):
        return iter(self.meta_dict.items())

    def parsed(self, string):
        # TODO: this parser shoudl work, but it doesn't seem to handle multiline :( Spec says we can use this.
        parsed = HeaderParser().parsestr(string)

        lines = string.split('\n')
        for line in lines:
            split = line.split(':')
            if len(split) == 1:
                value = split[0]
            else:
                key = split[0]
                value = ':'.join(split[1:])
            yield key, value

    def _metadata_from_pkginfo_string(self, string):
        """
        Extract metadata
        """
        metadata = {}
        # TODO: header parser doesn't seem to actually do multiline
        #parsed = HeaderParser().parsestr(string)
        parsed = self.parsed(string)
        for key, value in parsed:#.items():
            if key in constants.MULTI:
                if key not in metadata:
                    metadata[key] = []
                metadata[key].append(value)
            elif key in constants.TREAT_AS_MULTI:
                metadata[key] = value.split(',')
            else:
                metadata[key] = value

        return self._canonicalize(metadata)

    def _canonicalize(self, metadata):
        return {
            key.lower().replace('-', '_'): value
            for key, value in metadata.items()
        }

    def validate(self):
        base_validator = BaseMetadataValidator(self.meta_dict)
        if base_validator.validate():
            metadata_version = base_validator.metadata_version

            versioned_validator = {
                '1.2': Metadata1_2Validator
            }[metadata_version](self.meta_dict)

            versioned_validator.validate()
