MULTI = {}
TREAT_AS_MULTI = {}
SINGLE = {}
MULTI_1_0 = {
    "Platform",
    # "Supported-Platform", 1.1
    # "Classifier", 1.1
    # "Requires-Dist", 1.2
    # "Provides-Dist", 1.2
    # "Obsoletes-Dist", 1.2
    # "Requires-External", 1.2
    # "Project-URL", 1.2
    # "Provides-Extra", 2.1
}

TREAT_AS_MULTI_1_0 = {"Keywords"}

SINGLE_1_0 = {
    "Metadata-Version",
    "Name",
    "Version",
    "Summary",
    "Description",
    # "Description-Content-Type", 2.1
    "Home-page",
    # "Download-URL", 1.1
    "Author",
    "Author-email",
    # "Maintainer", 1.2
    # "Maintainer-email", 1.2
    "License",
    # "Requires-Python", 1.2
}


MULTI_1_1 = {"Platform", "Supported-Platform", "Classifier"}

TREAT_AS_MULTI_1_1 = {"Keywords"}

SINGLE_1_1 = {
    "Metadata-Version",
    "Name",
    "Version",
    "Summary",
    "Description",
    "Home-page",
    "Download-URL",
    "Author",
    "Author-email",
    "License",
}


MULTI_1_2 = {
    "Platform",
    "Supported-Platform",
    "Classifier",
    "Requires-Dist",
    "Provides-Dist",
    "Obsoletes-Dist",
    "Requires-External",
    "Project-URL",
}

TREAT_AS_MULTI_1_2 = {"Keywords"}

SINGLE_1_2 = {
    "Metadata-Version",
    "Name",
    "Version",
    "Summary",
    "Description",
    "Home-page",
    "Download-URL",
    "Author",
    "Author-email",
    "Maintainer",
    "Maintainer-email",
    "License",
    "Requires-Python",
}


MULTI_2_1 = {
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

TREAT_AS_MULTI_2_1 = {"Keywords"}

SINGLE_2_1 = {
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


VERSIONED_METADATA_FIELDS = {
    "1.0": {
        "MULTI": MULTI_1_0,
        "TREAT_AS_MULTI": TREAT_AS_MULTI_1_0,
        "SINGLE": SINGLE_1_0,
    },
    "1.1": {
        "MULTI": MULTI_1_1,
        "TREAT_AS_MULTI": TREAT_AS_MULTI_1_1,
        "SINGLE": SINGLE_1_1,
    },
    "1.2": {
        "MULTI": MULTI_1_2,
        "TREAT_AS_MULTI": TREAT_AS_MULTI_1_2,
        "SINGLE": SINGLE_1_2,
    },
    "2.1": {
        "MULTI": MULTI_2_1,
        "TREAT_AS_MULTI": TREAT_AS_MULTI_2_1,
        "SINGLE": SINGLE_2_1,
    },
}
