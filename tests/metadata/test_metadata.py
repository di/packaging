# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from packaging.metadata import Metadata
from . test_metadata_constants import VALID_PACKAGE_1_0, VALID_PACKAGE_1_2
import pytest
import os
class TestMetaData:
    
    def test_kwargs_init(self):
        metadata = Metadata(name="foo", version="1.0", keywords=["a", "b", "c"], description="Hello\nworld")
        assert metadata.meta_dict == {"name" : "foo", "version" : "1.0", "keywords": ["a", "b", "c"], "description" : "Hello\nworld"}

    def test_from_json(self):
        metadata_1 = Metadata(name="foo", version="1.0", keywords=["a", "b", "c"], description="Hello\nworld")
        metadata_2 = Metadata.from_json(r'{"name": "foo", "version": "1.0", "keywords": ["a", "b", "c"], "description": "Hello\nworld"}')

        assert metadata_1 == metadata_2

    def test_from_rfc822(self):
        metadata_1 = Metadata.from_rfc822(VALID_PACKAGE_1_0)
        metadata_2 = Metadata(metadata_version="1.0", name="test-package", version="0.1", summary="description", home_page="UNKNOWN", author="John Doe", author_email="blah@example.com", license="UNKNOWN", description="UNKNOWN", platform=["UNKNOWN"])

        assert metadata_1 == metadata_2, metadata_2.meta_dict

    def test_from_dict(self):
        metadata_1 = Metadata(name="foo", version="1.0", keywords=["a", "b", "c"], description="Hello\nworld")
        metadata_2 = Metadata.from_dict({"name": "foo", "version": "1.0", "keywords": ["a", "b", "c"], "description": "Hello\nworld"})

        assert metadata_1 == metadata_2

    @pytest.mark.parametrize(
        "filename",
        ["test_pkg.whl", "test_pkg.tar.gz", "test_pkg.zip", "test_pkg.tar.bz2"]
    )
    def test_from_file(self, filename):
        correct_metadata_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "METADATA")
        m_1 = Metadata.from_rfc822(open(correct_metadata_file).read())
        test_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        m_2 = Metadata.from_file(test_file)

        print(m_1.to_dict())
        print(m_2.to_dict())

        assert m_2 == m_1 
        

    def test_to_json(self):
        metadata_1 = Metadata(name="foo", version="1.0", keywords=["a", "b", "c"], description="Hello\nworld")
        json_data = metadata_1.to_json()
        metadata_2 = Metadata.from_json(json_data)

        assert metadata_1 == metadata_2

    def test_to_rfc822(self):
        metadata_1 = Metadata(name="foo", version="1.0", keywords=["a", "b", "c"], description="Hello\nworld")
        rfc822_data = metadata_1.to_rfc822()
        metadata_2 = Metadata.from_rfc822(rfc822_data)

        assert metadata_1 == metadata_2

