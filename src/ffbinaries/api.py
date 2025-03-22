"""ffbinaries API Client Module."""

__all__ = ['FFBinariesV1APIClient']

import logging
from typing import Any, Final, Literal

from requests import Response, Session

from ffbinaries.enums import (
    APIVersionType,
    ComponentType,
    HTTPMethodType,
    PlatformCodeType,
)
from ffbinaries.exceptions import (
    FFBinariesAPIClientError,
)
from ffbinaries.schemas.version import VersionResponseSchema, VersionsResponseSchema
from ffbinaries.utils import is_float


class FFBinariesV1APIClient:
    """ffbinaries API Client Class."""

    BASE_API_URL: Final[str] = 'https://ffbinaries.com/api'
    API_VERSION: Literal[APIVersionType.V1] = APIVersionType.V1

    ENDPOINT_VERSIONS: Final[str] = f'{BASE_API_URL}/{API_VERSION}/versions'
    ENDPOINT_VERSION: Final[str] = f'{BASE_API_URL}/{API_VERSION}/version'
    ENDPOINT_LATEST: Final[str] = f'{ENDPOINT_VERSION}/latest'
    ENDPOINT_EXACT_VERSION: Final[str] = f'{ENDPOINT_VERSION}/{{}}'

    DEFAULT_CACHE_AGE: Final[int] = 300
    DEFAULT_REQUEST_TIMEOUT: Final[int] = 60

    def __init__(self, request_timeout: int = DEFAULT_REQUEST_TIMEOUT) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._request_timeout = request_timeout

        self._session = Session()

    def _request(
        self,
        url: str,
        method: HTTPMethodType = HTTPMethodType.GET,
        stream: bool = False,
        jsonify: bool = False,
    ) -> Response | dict[str, Any]:
        """General Request Method."""
        return self.__make_request(
            url=url, method=method, stream=stream, jsonify=jsonify
        )

    def __make_request(
        self, url: str, method: HTTPMethodType, stream: bool, jsonify: bool
    ) -> Response | dict[str, Any]:
        self._log.debug('%s %s ', method, url)
        response = self._session.request(
            method=method, url=url, stream=stream, timeout=self._request_timeout
        )
        return response.json() if jsonify else response

    def _valid_for_caching(self, url: str) -> bool:
        return self.BASE_API_URL in url

    def get_latest_metadata(self) -> VersionResponseSchema:
        return VersionResponseSchema.model_validate_json(
            self._request(url=self.ENDPOINT_LATEST).text
        )

    def get_available_versions_metadata(self) -> VersionsResponseSchema:
        return VersionsResponseSchema.model_validate_json(
            self._request(url=self.ENDPOINT_VERSIONS).text
        )

    def get_exact_version_metadata(self, version: str) -> VersionResponseSchema:
        return VersionResponseSchema.model_validate_json(
            self._request(url=self.ENDPOINT_EXACT_VERSION.format(version)).text
        )

    def get_latest_version(self) -> str:
        return self.get_latest_metadata().version

    def get_available_versions(self) -> tuple[str, ...]:
        metadata = self.get_available_versions_metadata()
        # Check if version can be converted to float but use original
        # string version for compatibility with API response.
        # If got regular non-float string e.g. 'latest', skip it.
        return tuple(v for v in metadata.versions if is_float(value=v))

    def download_latest_version(
        self, component: ComponentType, platform: PlatformCodeType, stream: bool = False
    ) -> Response:
        try:
            url: str = self.get_latest_metadata().bin.model_dump()[platform][component]
        except KeyError as err:
            msg = f'Failed to download latest version: {err}'
            raise FFBinariesAPIClientError(msg) from err
        return self._request(url=url, stream=stream)

    def download_exact_version(
        self,
        component: ComponentType,
        version: str,
        platform: PlatformCodeType,
        stream: bool = False,
    ) -> Response:
        metadata = self.get_exact_version_metadata(version=version)
        try:
            url: str = metadata.bin.model_dump()[platform][component]
        except KeyError as err:
            msg = f'Failed to download exact version: {err}'
            raise FFBinariesAPIClientError(msg) from err
        return self._request(url=url, stream=stream)
