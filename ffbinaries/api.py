"""ffbinaries API client."""

import logging
import posixpath
import time

import requests

from ffbinaries.const import HTTP
from ffbinaries.exceptions import FFBinariesApiClientException
from ffbinaries.utils import retry

API_URL = 'https://ffbinaries.com/api'
DEFAULT_API_VERSION = 'v1'
ENDPOINT_VERSIONS = 'versions'
ENDPOINT_VERSION = 'version'
ENDPOINT_LATEST = '{0}/latest'.format(ENDPOINT_VERSION)
ENDPOINT_EXACT_VERSION = '{0}/{{0}}'.format(ENDPOINT_VERSION)


class FFBinariesApiClient:
    """ffbinaries API Class."""

    def __init__(self):
        pass

    def _request(self, url, method=HTTP.GET, stream=False):
        """General Request Method."""
        return requests.request(method=method, url=url, stream=stream)

    def get_latest_metadata(self, api_ver=DEFAULT_API_VERSION):
        url = posixpath.join(API_URL, api_ver, ENDPOINT_LATEST)
        return self._request(url=url).json()

    def get_available_versions_metadata(self, api_ver=DEFAULT_API_VERSION):
        url = posixpath.join(API_URL, api_ver, ENDPOINT_VERSIONS)
        return self._request(url=url).json()

    def get_exact_version_metadata(self, version, api_ver=DEFAULT_API_VERSION):
        url = posixpath.join(API_URL, api_ver,
                             ENDPOINT_EXACT_VERSION.format(version))
        return self._request(url=url).json()

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
        # Make only one request and use cached json metadata further.
        metadata = self.get_latest_metadata()['bin'][platform]
        return self._request(url=metadata[component], stream=stream)

    def download_exact_version(self, platform, component, version,
                               api_ver=DEFAULT_API_VERSION, stream=False):
        metadata = self.get_exact_version_metadata(version, api_ver)
        binary_url = metadata['bin'][platform][component]
        return self._request(url=binary_url, stream=stream)
