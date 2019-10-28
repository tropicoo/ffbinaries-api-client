"""Exceptions Module."""


class FFBinariesAPIClientError(Exception):
    """General API Client Error Class."""
    pass


class InvalidArgumentError(ValueError):
    """Invalid Argument Exception."""
    pass


class CacheError(Exception):
    """Base Cache Error Class."""
    pass


class NoCacheDataError(CacheError):
    """Raised when cache doesn't contain queried data."""

    def __str__(self):
        return 'No cache data'


class ExpiredCacheDataError(CacheError):
    """Expired Cache Data Error Class."""

    def __str__(self):
        return 'Expired cache data'
