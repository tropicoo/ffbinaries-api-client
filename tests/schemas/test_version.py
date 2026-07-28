from abc import ABC
from copy import deepcopy

import pytest
from pydantic import BaseModel

from ffbinaries.schemas.version import (
    BaseComponentSchema,
    BinSchema,
    VersionsResponseSchema,
)
from tests.schemas.conftest import (
    BASE_COMPONENT_SCHEMA_JSON_SCHEMA,
    BIN_SCHEMA_JSON_SCHEMA,
    PYDANTIC_COMPONENT_CLASSES,
    PYDANTIC_SCHEMAS,
    VERSIONS_RESPONSE_SCHEMA_JSON_SCHEMA,
)


def test_base_component_class() -> None:
    assert issubclass(BaseComponentSchema, ABC)


@pytest.mark.parametrize('cls', PYDANTIC_SCHEMAS)
def test_base_schemas_inherit_from_base_model(cls: type[BaseModel]) -> None:
    assert issubclass(cls, BaseModel)


@pytest.mark.parametrize(
    'cls', PYDANTIC_COMPONENT_CLASSES, ids=lambda cls: cls.__name__
)
def test_base_schemas_have_same_json_schema(cls: type[BaseComponentSchema]) -> None:
    expected_schema = deepcopy(BASE_COMPONENT_SCHEMA_JSON_SCHEMA)
    expected_schema['title'] = cls.__name__

    assert cls.model_json_schema() == expected_schema


def test_bin_schema_inheritance() -> None:
    assert issubclass(BinSchema, BaseModel)


def test_bin_schema_json_schema() -> None:
    assert BinSchema.model_json_schema() == BIN_SCHEMA_JSON_SCHEMA


def test_versions_response_schema_json_schema() -> None:
    assert (
        VersionsResponseSchema.model_json_schema()
        == VERSIONS_RESPONSE_SCHEMA_JSON_SCHEMA
    )
