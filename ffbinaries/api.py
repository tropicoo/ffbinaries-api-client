"""ffbinaries API Client Module."""

import logging
import posixpath
import time

import requests

from ffbinaries.const import HTTP
from ffbinaries.exceptions import FFBinariesApiClientException
from ffbinaries.utils import retry

BASE_API_URL = 'https://ffbinaries.com/api'
DEFAULT_API_VERSION = 'v1'

ENDPOINT_VERSIONS = 'versions'
ENDPOINT_VERSION = 'version'
ENDPOINT_LATEST = '{0}/latest'.format(ENDPOINT_VERSION)
ENDPOINT_EXACT_VERSION = '{0}/{{0}}'.format(ENDPOINT_VERSION)

CACHE_AGE = 300


class Cache:
    """Very Simple Cache Class."""

    __slots__ = ('_cache_age', '_cache')

    def __init__(self, cache_age):
        self._cache_age = cache_age
        self._cache = {}

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
        raise ValueError('No cached data')


class FFBinariesAPIClient:
    """ffbinaries API Client Class."""

    __slots__ = ('_use_caching', '_cache')

    def __init__(self, use_caching=False, cache_age=CACHE_AGE):
        self._use_caching = use_caching
        self._cache = Cache(cache_age) if use_caching else None

    def _request(self, url, method=HTTP.GET, stream=False, jsonify=False):
        """General Request Method."""
        def __make_request():
            response = requests.request(method=method, url=url, stream=stream)
            return response.json() if jsonify else response

        if self._use_caching and self._url_is_valid_for_caching(url):
            try:
                return self._cache.get(url)
            except ValueError:
                data = __make_request()
                self._cache.add(url, data)
                return data
        return __make_request()

    @staticmethod
    def _url_is_valid_for_caching(url):
        return BASE_API_URL in url

    def get_latest_metadata(self, api_ver=DEFAULT_API_VERSION):
        url = posixpath.join(BASE_API_URL, api_ver, ENDPOINT_LATEST)
        return self._request(url=url, jsonify=True)

    def get_available_versions_metadata(self, api_ver=DEFAULT_API_VERSION):
        url = posixpath.join(BASE_API_URL, api_ver, ENDPOINT_VERSIONS)
        return self._request(url=url, jsonify=True)

    def get_exact_version_metadata(self, version, api_ver=DEFAULT_API_VERSION):
        url = posixpath.join(BASE_API_URL, api_ver,
                             ENDPOINT_EXACT_VERSION.format(version))
        return self._request(url=url, jsonify=True)

    def get_latest_version(self):
        return float(self.get_latest_metadata()['version'])

    def get_available_versions(self):
        versions = []
        metadata = self.get_available_versions_metadata()
        for version in metadata['versions'].keys():
            try:
                versions.append(float(version))
            except ValueError:
                # Got regular non-float string e.g. 'latest'.
                pass
        versions.sort()
        return versions

    def download_latest_version(self, platform, component, stream=False):
        metadata = self.get_latest_metadata()['bin'][platform]
        return self._request(url=metadata[component], stream=stream)

    def download_exact_version(self, platform, component, version,
                               api_ver=DEFAULT_API_VERSION, stream=False):
        metadata = self.get_exact_version_metadata(version, api_ver)
        binary_url = metadata['bin'][platform][component]
        return self._request(url=binary_url, stream=stream)
