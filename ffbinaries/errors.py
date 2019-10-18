"""Exceptions Module."""


class FFBinariesAPIClientError(Exception):
    pass


class InvalidArgumentError(ValueError):
    pass


class NoCachedDataError(Exception):
    pass
