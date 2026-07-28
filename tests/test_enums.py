import pytest

from ffbinaries.enums import (
    APIVersionType,
    BaseStrChoiceEnum,
    ComponentType,
    HTTPMethodType,
    PlatformCodeType,
)


def test_base_str_choice_enum() -> None:
    assert hasattr(BaseStrChoiceEnum, 'choices')
    assert callable(BaseStrChoiceEnum.choices)


@pytest.mark.parametrize(
    ('enum_cls', 'expected'),
    [
        (
            HTTPMethodType,
            (
                'DELETE',
                'GET',
                'HEAD',
                'OPTIONS',
                'PATCH',
                'POST',
                'PUT',
            ),
        ),
        (APIVersionType, ('v1',)),
        (
            PlatformCodeType,
            (
                'windows-32',
                'windows-64',
                'linux-32',
                'linux-64',
                'linux-armhf',
                'linux-armel',
                'linux-arm64',
                'osx-64',
            ),
        ),
        (
            ComponentType,
            (
                'ffmpeg',
                'ffplay',
                'ffprobe',
                'ffserver',
            ),
        ),
    ],
)
def test_choices(enum_cls: type[BaseStrChoiceEnum], expected: tuple[str, ...]) -> None:
    assert enum_cls.choices() == expected


@pytest.mark.parametrize(
    'enum_cls',
    [
        HTTPMethodType,
        APIVersionType,
        PlatformCodeType,
        ComponentType,
    ],
)
def test_members_are_strings(enum_cls: type[BaseStrChoiceEnum]) -> None:
    for member in enum_cls:
        assert isinstance(member, str)
        assert member == member.value


@pytest.mark.parametrize(
    'enum_cls',
    [
        HTTPMethodType,
        APIVersionType,
        PlatformCodeType,
        ComponentType,
    ],
)
def test_choices_contains_all_values(enum_cls: type[BaseStrChoiceEnum]) -> None:
    assert enum_cls.choices() == tuple(member.value for member in enum_cls)
