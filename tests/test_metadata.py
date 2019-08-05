# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.
from __future__ import absolute_import, division, print_function

from packaging.metadata import Metadata

class TestMetadata:
    def test_validate(self):
        m = Metadata(filename='test_data/mudpy-0.0.1.dev232.tar.gz')
        m.validate()

    def test_invalid_license_text(self):
        # this has an invalid (multiline) summary. It also has a multiline license tha tisn't proerply
        # indented.
        # Suggest making a runner that makes these packages so
        # we can automate test data? for now coul have multiple zips though
        m = Metadata(filename='test_data/test-package-0.1.tar.gz')
        m.validate()

