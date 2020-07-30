# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from packaging.metadata import Metadata
from . test_metadata_constants import VALID_PACKAGE_1_2_JSON, VALID_PACKAGE_1_2_RFC822, VALID_PACKAGE_1_2_DICT, VALID_PACKAGE_1_0_WITH_DESC_REPEATED, VALID_PACKAGE_1_0_WITH_DESC_RFC822, VALID_PACKAGE_1_0_WITH_DESC_JSON, VALID_PACKAGE_1_0_WITH_DESC_DICT, VALID_PACKAGE_2_1_RFC822, VALID_PACKAGE_2_1_JSON, VALID_PACKAGE_2_1_DICT, VALID_PACKAGE_1_1_RFC822, VALID_PACKAGE_1_1_JSON, VALID_PACKAGE_1_1_DICT
import pytest
import os
from packaging.metadata.exceptions import UnknownDistributionFormat, NoMetadataFound, MultipleMetadataFound


class TestMetaData:
    
    def test_kwargs_init(self):
        metadata = Metadata(name="foo", version="1.0", keywords=["a", "b", "c"], description="Hello\nworld")
        assert metadata.meta_dict == {"name" : "foo", "version" : "1.0", "keywords": ["a", "b", "c"], "description" : "Hello\nworld"}

    @pytest.mark.parametrize(
        ("metadata_dict" , "metadata_json"),
        [(VALID_PACKAGE_1_2_DICT, VALID_PACKAGE_1_2_JSON),
        (VALID_PACKAGE_1_0_WITH_DESC_DICT, VALID_PACKAGE_1_0_WITH_DESC_JSON),
        (VALID_PACKAGE_2_1_DICT, VALID_PACKAGE_2_1_JSON),
        (VALID_PACKAGE_1_1_DICT, VALID_PACKAGE_1_1_JSON)
        ]
    )
    def test_from_json(self, metadata_dict, metadata_json):
        metadata_1 = Metadata(**metadata_dict)
        metadata_2 = Metadata.from_json(metadata_json)

        assert metadata_1 == metadata_2

    @pytest.mark.parametrize(
        ("metadata_dict", "metadata_rfc822"),
        [(VALID_PACKAGE_1_2_DICT, VALID_PACKAGE_1_2_RFC822),
        (VALID_PACKAGE_1_0_WITH_DESC_DICT, VALID_PACKAGE_1_0_WITH_DESC_RFC822),
        (VALID_PACKAGE_2_1_DICT, VALID_PACKAGE_2_1_RFC822),
        (VALID_PACKAGE_1_1_DICT, VALID_PACKAGE_1_1_RFC822)
        ]
    )
    def test_from_rfc822(self, metadata_dict, metadata_rfc822):
        metadata_1 = Metadata(**metadata_dict)
        metadata_2 = Metadata.from_rfc822(metadata_rfc822)

        assert metadata_1 == metadata_2

    @pytest.mark.parametrize(
        ("metadata_dict", "metadata_json"),
        [(VALID_PACKAGE_1_2_DICT, VALID_PACKAGE_1_2_JSON),
        (VALID_PACKAGE_1_0_WITH_DESC_DICT, VALID_PACKAGE_1_0_WITH_DESC_JSON),
        (VALID_PACKAGE_2_1_DICT, VALID_PACKAGE_2_1_JSON),
        (VALID_PACKAGE_1_1_DICT, VALID_PACKAGE_1_1_JSON)
        ]
    )
    def test_from_dict(self, metadata_dict, metadata_json):
        metadata_1 = Metadata.from_dict(metadata_dict)
        metadata_2 = Metadata.from_json(metadata_json)

        assert metadata_1 == metadata_2

    @pytest.mark.parametrize(
        "filename",
        ["test_pkg.whl", "test_pkg.tar.gz", "test_pkg.zip", "test_pkg.tar.bz2"]
    )
    def test_from_file(self, filename):
        correct_metadata_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "PKG-INFO")
        m_1 = Metadata.from_rfc822(open(correct_metadata_file).read())
        test_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        m_2 = Metadata.from_file(test_file)

        #For the .whl test case we need to add 2 "\n"s to the description, like the wheel module does
        _ , extension = os.path.splitext(filename)
        if extension == ".whl":
            m_1.meta_dict["description"] = m_1.meta_dict["description"] + "\n\n"
        
        assert m_2 == m_1 
    
    @pytest.mark.parametrize(
        "filename",
        ["test_pkg.jpg", "test_pkg.txt", "test_pkg.lib"]
    )
    def test_from_file_bad_extension(self, filename):
        with pytest.raises(UnknownDistributionFormat):
            Metadata.from_file(filename)


    @pytest.mark.parametrize(
        "metadata_json",
        [VALID_PACKAGE_1_2_JSON, VALID_PACKAGE_1_0_WITH_DESC_JSON, VALID_PACKAGE_1_1_JSON, VALID_PACKAGE_2_1_JSON]
    )
    def test_to_json(self, metadata_json):
        metadata_1 = Metadata.from_json(metadata_json)
        generated_json = metadata_1.to_json()
        metadata_2 = Metadata.from_json(generated_json)

        assert metadata_1 == metadata_2

    @pytest.mark.parametrize(
        "metadata_rfc822",
        [VALID_PACKAGE_1_2_RFC822, VALID_PACKAGE_1_0_WITH_DESC_RFC822, VALID_PACKAGE_1_1_RFC822, VALID_PACKAGE_2_1_RFC822]
    )
    def test_to_rfc822(self, metadata_rfc822):
        metadata_1 = Metadata.from_rfc822(metadata_rfc822)
        generated_rfc822 = metadata_1.to_rfc822()
        metadata_2 = Metadata.from_rfc822(generated_rfc822)

        assert metadata_1 == metadata_2

    @pytest.mark.parametrize(
        "metadata_dict",
        [VALID_PACKAGE_1_2_DICT, VALID_PACKAGE_1_0_WITH_DESC_DICT, VALID_PACKAGE_1_1_DICT, VALID_PACKAGE_2_1_DICT]
    )
    def test_to_dict(self, metadata_dict):
        metadata_1 = Metadata.from_dict(metadata_dict)
        generated_dict = metadata_1.to_dict()
        metadata_2 = Metadata.from_dict(generated_dict)

        assert metadata_1 == metadata_2

    def test_metadata_iter(self):
        metadata_1 = Metadata(name="foo", version="1.0", keywords=["a", "b", "c"], description="Hello\nworld")

        for key, value in metadata_1.__iter__():
            assert key in metadata_1.meta_dict
            assert metadata_1.meta_dict[key] == value

    def test_repeated_description_in_metadata(self):
        metadata_1 = Metadata.from_rfc822(VALID_PACKAGE_1_0_WITH_DESC_REPEATED)

        assert metadata_1.meta_dict["description"] == "# Example Package\n\nThis is a simple example package to test pypa/packaging"

    def test_metadata_validation(self):
        #Validation not currently implemented
        with pytest.raises(NotImplementedError):
            metadata = Metadata(name="foo", version="1.0", keywords=["a", "b", "c"], description="Hello\nworld")
            metadata.validate()
    
    def test_metadata_equals_different_order(self):
        metadata_1 = Metadata(name="foo", version="1.0", keywords=["a", "b", "c"], description="Hello\nworld")
        metadata_2 = Metadata(version="1.0", keywords=["a", "b", "c"], description="Hello\nworld", name="foo")

        assert metadata_1 == metadata_2
    
    def test_metadata_equals_non_metadata(self):
        metadata_1 = Metadata(name="foo", version="1.0", keywords=["a", "b", "c"], description="Hello\nworld")
        assert metadata_1.__eq__({"name" : "foo", "version" : "1.0", "keywords": ["a", "b", "c"], "description" : "Hello\nworld"}) == False
