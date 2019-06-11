from email.parser import HeaderParser

multi = {
    'Platform',
    'Supported-Platform',
    'Classifier',
    'Requires-Dist',
    'Provides-Dist',
    'Obsoletes-Dist',
    'Requires-External',
    'Project-URL',
    'Provides-Extra',
}

treat_as_multi = {
    'Keywords',
}


def canonicalize(metadata):
    """
    Transforms a metadata object to the canonical representation
    as specified in
    https://www.python.org/dev/peps/pep-0566/#json-compatible-metadata
    All transformed keys should be reduced to lower case. Hyphens
    should be replaced with underscores, but otherwise should retain all
    other characters.
    """
    return {
        key.lower().replace('-', '_'): value
        for key, value in metadata.items()
    }


def extract_metadata(string):
    """Extracts metadata information from a metadata-version 2.1 object.

    https://www.python.org/dev/peps/pep-0566/#json-compatible-metadata

    - The original key-value format should be read with email.parser.HeaderParser;
    - All transformed keys should be reduced to lower case. Hyphens should be replaced with underscores, but otherwise should retain all other characters;
    - The transformed value for any field marked with "(Multiple-use") should be a single list containing all the original values for the given key;
    - The Keywords field should be converted to a list by splitting the original value on whitespace characters;
    - The message body, if present, should be set to the value of the description key.
    - The result should be stored as a string-keyed dictionary.
    """
    metadata = {}
    parsed = HeaderParser().parsestr(string)
    for key, value in parsed.items():
        if key in multi:
            if key not in metadata:
                metadata[key] = []
            metadata[key].append(value)
        elif key in treat_as_multi:
            metadata[key] = value.split(',')
        else:
            metadata[key] = value

    return canonicalize(metadata)
