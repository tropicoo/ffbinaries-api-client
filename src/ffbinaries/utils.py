"""Utils Module."""

__all__ = ['is_float']


def is_float(value: str) -> bool:
    """Check if value is a float."""
    try:
        float(value)
    except ValueError:
        return False
    return True
