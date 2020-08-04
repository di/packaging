VERSIONED_METADATA_FIELDS = {
    "1.0": {"MULTI": {}, "TREAT_AS_MULTI": {}, "SINGLE": {}},
    "1.1": {"MULTI": {}, "TREAT_AS_MULTI": {}, "SINGLE": {}},
    "1.2": {"MULTI": {}, "TREAT_AS_MULTI": {}, "SINGLE": {}},
    "2.1": {"MULTI": {}, "TREAT_AS_MULTI": {}, "SINGLE": {}},
}


MULTI = {
    "Platform",
    "Supported-Platform",
    "Classifier",
    "Requires-Dist",
    "Provides-Dist",
    "Obsoletes-Dist",
    "Requires-External",
    "Project-URL",
    "Provides-Extra",
}

TREAT_AS_MULTI = {"Keywords"}

SINGLE = {
    "Metadata-Version",
    "Name",
    "Version",
    "Summary",
    "Description",
    "Description-Content-Type",
    "Home-page",
    "Download-URL",
    "Author",
    "Author-email",
    "Maintainer",
    "Maintainer-email",
    "License",
    "Requires-Python",
}
