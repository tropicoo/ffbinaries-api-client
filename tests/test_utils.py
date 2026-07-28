from hypothesis import given
from hypothesis import strategies as st

from ffbinaries.utils import is_float


@given(st.floats(allow_nan=True, allow_infinity=True))
def test_stringified_floats_are_valid(value: float) -> None:
    assert is_float(str(value))


@given(st.text())
def test_is_float_agrees_with_float(value: str) -> None:
    try:
        float(value)
    except ValueError:
        assert not is_float(value)
    else:
        assert is_float(value)
