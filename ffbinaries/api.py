"""ffbinaries API Client Module."""

import logging
import posixpath
from multiprocessing import Lock as proc_lock
from threading import Lock as thread_lock

import requests

from ffbinaries.cache import SimpleCache
from ffbinaries.const import HTTP
from ffbinaries.errors import (FFBinariesAPIClientError, NoCacheDataError,
                               ExpiredCacheDataError)
from ffbinaries.utils import retry

BASE_API_URL = 'https://ffbinaries.com/api'
DEFAULT_API_VERSION = 'v1'

ENDPOINT_VERSIONS = 'versions'
ENDPOINT_VERSION = 'version'
ENDPOINT_LATEST = '{0}/latest'.format(ENDPOINT_VERSION)
ENDPOINT_EXACT_VERSION = '{0}/{{0}}'.format(ENDPOINT_VERSION)

CACHE_AGE = 300

PROC_LOCK = proc_lock()
THREAD_LOCK = thread_lock()


class FFBinariesAPIClient:
    """ffbinaries API Client Class."""

    def __init__(self, use_caching=False, cache_age=CACHE_AGE, log_init=None):

        if log_init is not None and callable(log_init[0]):
            log_init[0](log_init[1])
        self._log = logging.getLogger(self.__class__.__name__)

        self._use_caching = use_caching
        self._cache = SimpleCache(cache_age)

    def _request(self, url, method=HTTP.GET, stream=False, jsonify=False):
        """General Request Method."""
        # Cache only JSON-data which should be directly returned to the caller.
        if all([jsonify, self._use_caching, self._valid_for_caching(url)]):
            with THREAD_LOCK, PROC_LOCK:
                try:
                    return self._cache.get(url)
                except (ExpiredCacheDataError, NoCacheDataError):
                    data = self.__make_request(url, method, stream, jsonify)
                    self._cache.add(url, data)
                    return data
        return self.__make_request(url, method, stream, jsonify)

    @retry()
    def __make_request(self, url, method, stream, jsonify):
        self._log.debug('%s %s ', method, url)
        response = requests.request(method=method, url=url, stream=stream)
        return response.json() if jsonify else response

    @staticmethod
    def _valid_for_caching(url):
        return BASE_API_URL in url

    def get_latest_metadata(self, api_ver=DEFAULT_API_VERSION):
        url = posixpath.join(BASE_API_URL, api_ver, ENDPOINT_LATEST)
        return self._request(url, jsonify=True)

    def get_available_versions_metadata(self, api_ver=DEFAULT_API_VERSION):
        url = posixpath.join(BASE_API_URL, api_ver, ENDPOINT_VERSIONS)
        return self._request(url, jsonify=True)

    def get_exact_version_metadata(self, version, api_ver=DEFAULT_API_VERSION):
        url = posixpath.join(BASE_API_URL, api_ver,
                             ENDPOINT_EXACT_VERSION.format(version))
        return self._request(url, jsonify=True)

    def get_latest_version(self):
        try:
            return self.get_latest_metadata()['version']
        except KeyError as err:
            raise FFBinariesAPIClientError('Failed to get latest published'
                                           'version: {0}'.format(err))

    def get_available_versions(self):
        versions = []
        metadata = self.get_available_versions_metadata()
        try:
            versions_view = metadata['versions'].keys()
        except KeyError as err:
            raise FFBinariesAPIClientError('Failed to get available versions:'
                                           ' {0}'.format(err))
        for version in versions_view:
            try:
                # Check if version can be converted to float but use original
                # string version for compatibility with API response.
                float_ver = float(version)
                versions.append(version)
            except ValueError:
                # Got regular non-float string e.g. 'latest', skip it.
                pass

        return versions

    def download_latest_version(self, component, platform, stream=False):
        try:
            url = self.get_latest_metadata()['bin'][platform][component]
        except KeyError as err:
            raise FFBinariesAPIClientError('Failed to download latest version:'
                                           ' {0}'.format(err))
        return self._request(url, stream=stream)

    def download_exact_version(self, component, version, platform,
                               api_ver=DEFAULT_API_VERSION, stream=False):
        metadata = self.get_exact_version_metadata(version, api_ver)
        try:
            url = metadata['bin'][platform][component]
        except KeyError as err:
            raise FFBinariesAPIClientError('Failed to download exact version:'
                                           ' {0}'.format(err))
        return self._request(url, stream=stream)

    def show_cache(self):
        return self._cache.get_cached_items()
