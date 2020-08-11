# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from packaging.metadata import Metadata
from packaging.metadata.distributions import Distribution

# from .test_metadata_constants import VALID_PACKAGE_2_1_RFC822, VALID_PACKAGE_2_1_JSON, VALID_PACKAGE_2_1_DICT, VALID_PACKAGE_1_0_RFC822, VALID_PACKAGE_1_0_DICT, VALID_PACKAGE_1_0_JSON, VALID_PACKAGE_1_0_RFC822, VALID_PACKAGE_1_1_RFC822, VALID_PACKAGE_1_1_DICT, VALID_PACKAGE_1_1_JSON, VALID_PACKAGE_1_2_RFC822, VALID_PACKAGE_1_2_DICT, VALID_PACKAGE_1_2_JSON
from .test_metadata_constants import *
import pytest
import os
from packaging.metadata.exceptions import (
    UnknownDistributionFormat,
    NoMetadataFound,
    MultipleMetadataFound,
)
import json


class TestMetaData:
    def test_kwargs_init(self):
        metadata = Metadata(
            name="foo",
            version="1.0",
            keywords=["a", "b", "c"],
            description="Hello\nworld",
        )
        assert metadata.meta_dict == {
            "name": "foo",
            "version": "1.0",
            "keywords": ["a", "b", "c"],
            "description": "Hello\nworld",
        }

    @pytest.mark.parametrize(
        ("metadata_dict", "metadata_json"),
        [
            (VALID_PACKAGE_2_1_DICT, VALID_PACKAGE_2_1_JSON),
            (VALID_PACKAGE_1_0_DICT, VALID_PACKAGE_1_0_JSON),
            (VALID_PACKAGE_1_1_DICT, VALID_PACKAGE_1_1_JSON),
            (VALID_PACKAGE_1_2_DICT, VALID_PACKAGE_1_2_JSON),
        ],
    )
    def test_from_json(self, metadata_dict, metadata_json):
        metadata_1 = Metadata(**metadata_dict)
        metadata_2 = Metadata.from_json(metadata_json)

        assert metadata_1 == metadata_2

    @pytest.mark.parametrize(
        ("metadata_dict", "metadata_rfc822"),
        [
            (VALID_PACKAGE_2_1_DICT, VALID_PACKAGE_2_1_RFC822),
            (VALID_PACKAGE_1_0_DICT, VALID_PACKAGE_1_0_RFC822),
            (VALID_PACKAGE_1_1_DICT, VALID_PACKAGE_1_1_RFC822),
            (VALID_PACKAGE_1_2_DICT, VALID_PACKAGE_1_2_RFC822),
        ],
    )
    def test_from_rfc822(self, metadata_dict, metadata_rfc822):
        metadata_1 = Metadata(**metadata_dict)
        metadata_2 = Metadata.from_rfc822(metadata_rfc822)

        assert metadata_1 == metadata_2

    @pytest.mark.parametrize(
        ("metadata_dict", "metadata_json"),
        [
            (VALID_PACKAGE_2_1_DICT, VALID_PACKAGE_2_1_JSON),
            (VALID_PACKAGE_1_0_DICT, VALID_PACKAGE_1_0_JSON),
            (VALID_PACKAGE_1_1_DICT, VALID_PACKAGE_1_1_JSON),
            (VALID_PACKAGE_1_2_DICT, VALID_PACKAGE_1_2_JSON),
        ],
    )
    def test_from_dict(self, metadata_dict, metadata_json):
        metadata_1 = Metadata.from_dict(metadata_dict)
        metadata_2 = Metadata.from_json(metadata_json)

        assert metadata_1 == metadata_2

    @pytest.mark.parametrize(
        "filename", ["test.whl", "test.tar.gz", "test.zip", "test.tar.bz2"]
    )
    def test_from_file(self, filename):
        m_1 = Metadata.from_rfc822(VALID_PACKAGE_2_1_RFC822)
        test_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        m_2 = Metadata.from_file(test_file)

        # For the .whl test case we need to add 2 "\n"s to the description, like the wheel module does
        _, extension = os.path.splitext(filename)
        if extension == ".whl":
            m_1.meta_dict["description"] = m_1.meta_dict["description"] + "\n\n"

        assert m_2 == m_1

    @pytest.mark.parametrize(
        "filename", ["test_pkg.jpg", "test_pkg.txt", "test_pkg.lib"]
    )
    def test_from_file_bad_extension(self, filename):
        with pytest.raises(UnknownDistributionFormat):
            Metadata.from_file(filename)

    @pytest.mark.parametrize(
        ("expected_json_string", "input_dict"),
        [
            (VALID_PACKAGE_1_2_JSON, VALID_PACKAGE_1_2_DICT),
            (VALID_PACKAGE_1_0_JSON, VALID_PACKAGE_1_0_DICT),
            (VALID_PACKAGE_1_1_JSON, VALID_PACKAGE_1_1_DICT),
            (VALID_PACKAGE_2_1_JSON, VALID_PACKAGE_2_1_DICT),
        ],
    )
    def test_to_json(self, expected_json_string, input_dict):
        metadata_1 = Metadata(**input_dict)
        generated_json_string = metadata_1.to_json()

        print("Expected json string:")
        print(expected_json_string)
        print("\n\nGenerated json string:")
        print(generated_json_string)

        assert expected_json_string == generated_json_string

    # @pytest.mark.parametrize(
    #     ("expected_rfc822_string", "input_dict"),
    #     [(VALID_PACKAGE_1_2_RFC822, VALID_PACKAGE_2_1_DICT), (VALID_PACKAGE_1_0_RFC822, VALID_PACKAGE_1_0_DICT),
    #     (VALID_PACKAGE_1_1_RFC822, VALID_PACKAGE_1_1_DICT), (VALID_PACKAGE_1_2_RFC822, VALID_PACKAGE_1_2_DICT)]
    # )
    # def test_to_rfc822(self, expected_rfc822_string, input_dict):
    #     metadata_1 = Metadata(**input_dict)
    #     generated_rfc822_string = metadata_1.to_rfc822()

    #     print("Expected RFC822:")
    #     print(expected_rfc822_string)
    #     print("\n\nGenerated RFC822:")
    #     print(generated_rfc822_string)
    #     print("Generated metadata dict:")
    #     print(Metadata.from_rfc822(generated_rfc822_string).to_dict())
    #     assert expected_rfc822_string == generated_rfc822_string

    @pytest.mark.parametrize(
        "expected_dict",
        [
            VALID_PACKAGE_1_2_DICT,
            VALID_PACKAGE_1_0_DICT,
            VALID_PACKAGE_1_1_DICT,
            VALID_PACKAGE_2_1_DICT,
        ],
    )
    def test_to_dict(self, expected_dict):
        metadata_1 = Metadata(**expected_dict)
        generated_dict = metadata_1.to_dict()

        assert expected_dict == generated_dict

    def test_metadata_iter(self):
        metadata_1 = Metadata(
            name="foo",
            version="1.0",
            keywords=["a", "b", "c"],
            description="Hello\nworld",
        )

        for key, value in metadata_1.__iter__():
            assert key in metadata_1.meta_dict
            assert metadata_1.meta_dict[key] == value

    def test_repeated_description_in_rfc822(self):
        metadata_1 = Metadata.from_rfc822(VALID_PACKAGE_1_0_REPEATED_DESC)

        assert (
            metadata_1.meta_dict["description"]
            == "# This is the long description \n\nThis will overwrite the Description field\n"
        )

    def test_single_line_description_in_rfc822(self):
        metdata_1 = Metadata.from_rfc822(VALID_PACKAGE_1_0_SINGLE_LINE_DESC)

        description = metdata_1.meta_dict["description"]

        assert len(description.splitlines()) == 1

    def test_metadata_validation(self):
        # Validation not currently implemented
        with pytest.raises(NotImplementedError):
            metadata = Metadata(
                name="foo",
                version="1.0",
                keywords=["a", "b", "c"],
                description="Hello\nworld",
            )
            metadata.validate()

    def test_metadata_equals_different_order(self):
        metadata_1 = Metadata(
            name="foo",
            version="1.0",
            keywords=["a", "b", "c"],
            description="Hello\nworld",
        )
        metadata_2 = Metadata(
            version="1.0",
            keywords=["a", "b", "c"],
            description="Hello\nworld",
            name="foo",
        )

        assert metadata_1 == metadata_2

    def test_metadata_equals_non_metadata(self):
        metadata_1 = Metadata(
            name="foo",
            version="1.0",
            keywords=["a", "b", "c"],
            description="Hello\nworld",
        )
        assert (
            metadata_1.__eq__(
                {
                    "name": "foo",
                    "version": "1.0",
                    "keywords": ["a", "b", "c"],
                    "description": "Hello\nworld",
                }
            )
            == False
        )

    def test_valid_custom_filetype(self, monkeypatch):
        class custom_distribution_class(Distribution):
            pass

        monkeypatch.setattr(
            custom_distribution_class,
            "extract_pkginfo",
            lambda _: VALID_PACKAGE_1_0_RFC822,
        )
        metadata_1 = Metadata.from_file("custom_dist.xz", custom_distribution_class)

        assert metadata_1

    def test_invalid_custom_filetype(self):
        class custom_distribution_class:
            pass

        with pytest.raises(UnknownDistributionFormat):
            Metadata.from_file("custom_dist.xz", custom_distribution_class)

    def test_test(self):
        metadata_1 = Metadata.from_rfc822(VALID_PACKAGE_1_0_REPEATED_DESC)
        print(metadata_1.to_dict())
