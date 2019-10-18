"""Simple Cache Module."""

import time

from ffbinaries.errors import InvalidArgumentError, NoCachedDataError


class SimpleCache:
    """Very Simple Cache Class."""

    def __init__(self, cache_age):

        if not isinstance(cache_age, (int, float)) or cache_age <= 0:
            raise InvalidArgumentError('cache_age value needs to be int or '
                                       'float and greater than 0')

        self._cache_age = cache_age
        self._cache = {}

    def get_cached_items(self):
        return self._cache

    def add(self, url, data):
        self._cache[url] = (int(time.time()), data)

    def get(self, url):
        try:
            if int(time.time()) - self._cache[url][0] < self._cache_age:
                return self._cache[url][1]
        except KeyError:
            self.__raise_no_cached_data()
        del self._cache[url]
        self.__raise_no_cached_data()

    @staticmethod
    def __raise_no_cached_data():
        raise NoCachedDataError('No cached data')
