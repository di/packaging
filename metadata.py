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
    return {
        key.lower().replace('-', '_'): value
        for key, value in metadata.items()
    }


def extract_metadata(string):
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
