# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.
from __future__ import absolute_import, division, print_function

from packaging.metadata import Metadata

class TestMetadata:
    def test_validate(self):
        m = Metadata(filename='../test_data/mudpy-0.0.1.dev232.tar.gz')
        m.validate()
