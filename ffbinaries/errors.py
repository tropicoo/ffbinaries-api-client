"""Exceptions Module."""


class FFBinariesApiClientError(Exception):
    pass


class InvalidArgumentError(ValueError):
    pass


class NoCachedDataError(Exception):
    pass
