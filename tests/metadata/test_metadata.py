# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.
from __future__ import absolute_import, division, print_function

from packaging.metadata import Metadata
from tests.metadata import test_metadata_constants as pkg_info

import tempfile
import io
import tarfile


class TestMetadata:
    def test_validate_1_0(self):
        m = Metadata(string=pkg_info.VALID_PACKAGE_1_0)
        m.validate()

    def test_validate_1_2(self):
        m = Metadata(string=pkg_info.VALID_PACKAGE_1_2)
        m.validate()

    def test_invalid_license_text(self):
        # this has an invalid (multiline) summary. It also has a multiline license that isn't proerply
        # indented.
        # Suggest making a runner that makes these packages so
        # we can automate test data? for now coul have multiple zips though
        m = Metadata(string=pkg_info.INVALID_LICENSE_1_0)
        m.validate()
