"""Constants Module."""


class _HTTPMethods:
    """HTTP Methods Class."""
    __slots__ = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

    def __init__(self):
        for method in self.__slots__:
            setattr(self, method, method)


HTTP = _HTTPMethods()
