class MetadataException(Exception):
    pass


class UnknownDistributionFormat(MetadataException):
    pass


class NoMetadataFound(MetadataException):
    pass


class MultipleMetadataFound(MetadataException):
    pass


class UnknownCustomDistributionFormat(MetadataException):
    pass
