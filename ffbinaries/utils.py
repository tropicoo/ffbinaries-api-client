"""Utils module."""

import time
from functools import wraps


def retry(delay=5, retries=3):
    """Retry decorator."""
    retries = retries if retries > 0 else 1

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _err = None
            for ret in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    time.sleep(delay)
                    _err = err
            else:
                raise _err

        return wrapper

    return decorator
