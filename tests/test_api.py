"""Unittests for Updater API."""

import time
import unittest
from unittest.mock import patch, PropertyMock

import requests

from ffbinaries import FFBinariesAPIClient
import jsons

LOG_LEVEL = 3  # DEBUG

LATEST_VERSION = '4.2'

WIN_32 = 'windows-32'
WIN_64 = 'windows-64'
PLATFORM_MAP = {WIN_32: 'win-32',
                WIN_64: 'win-64'}

COMPONENTS = ('ffmpeg', 'ffplay', 'ffprobe')
NON_EXISTENT_COMPONENT = 'ffserver'

FILENAME_PATTERN_FF = '{component}-{version}-{platform}.zip'
HEADER_CONTENT_LENGTH = 'Content-Length'
HEADER_CONTENT_DISPOSITION = 'Content-Disposition'
HEADER_CONTENT_DISPOSITION_VALUE = 'attachment; filename={filename}'

STATUS_CODE_OK = 200

BINARY_CONTENT_DUMMY = b'<binary_content>'

API_VERSIONS = 'https://ffbinaries.com/api/v1/versions'
API_LATEST = 'https://ffbinaries.com/api/v1/version/latest'
API_VERSION_3_3 = 'https://ffbinaries.com/api/v1/version/3.3'

AVAILABLE_VERSIONS_LIST = ['3.2', '3.3', '3.4', '4.0', '4.1', '4.2']


def make_response(content_disposition_value):
    res = requests.models.Response()
    res.status_code = STATUS_CODE_OK
    type(res).content = PropertyMock(return_value=BINARY_CONTENT_DUMMY)
    res.headers = {HEADER_CONTENT_DISPOSITION: content_disposition_value,
                   HEADER_CONTENT_LENGTH: str(len(BINARY_CONTENT_DUMMY))}
    return res


class TestFFBinariesAPIClient(unittest.TestCase):
    def setUp(self):
        self._api = FFBinariesAPIClient()
        self._platforms = (WIN_32, WIN_64)

    def _verify_data(self, obj, platform, component):
        self.assertIsInstance(obj, requests.models.Response)
        self.assertEqual(obj.status_code, STATUS_CODE_OK)

        self.assertEqual(len(obj.content),
                         int(obj.headers[HEADER_CONTENT_LENGTH]))

        self.assertEqual(obj.headers[HEADER_CONTENT_DISPOSITION],
                         HEADER_CONTENT_DISPOSITION_VALUE.format(
                             filename=FILENAME_PATTERN_FF.format(
                                 component=component,
                                 version=LATEST_VERSION,
                                 platform=platform)))

    @patch('ffbinaries.FFBinariesAPIClient.get_latest_metadata',
           return_value=jsons.LATEST_METADATA)
    @patch.object(requests, 'request')
    def test_download_latest_version(self, mock_request, get_latest_metadata_mock):
        for platform in self._platforms:
            for comp in COMPONENTS:
                filename_platform = PLATFORM_MAP[platform]
                header_value = HEADER_CONTENT_DISPOSITION_VALUE.format(
                    filename=FILENAME_PATTERN_FF.format(component=comp,
                                                        platform=filename_platform,
                                                        version=LATEST_VERSION))
                mock_request.return_value = make_response(header_value)
                obj = self._api.download_latest_version(platform=platform,
                                                        component=comp)
                self._verify_data(obj, filename_platform, comp)
                self._api.get_latest_metadata.assert_called_once()

                url = jsons.LATEST_METADATA['bin'][platform][comp]
                requests.request.assert_called_once_with(method='GET',
                                                         url=url,
                                                         stream=False)
                self._api.get_latest_metadata.reset_mock()
                requests.request.reset_mock()

    @patch('ffbinaries.FFBinariesAPIClient.get_latest_metadata',
           return_value=jsons.LATEST_METADATA)
    def test_get_latest_version(self, get_latest_metadata_mock):
        version = self._api.get_latest_version()
        self.assertEqual(version, LATEST_VERSION)
        self._api.get_latest_metadata.assert_called_once()

    @patch('ffbinaries.FFBinariesAPIClient._request')
    def test_get_latest_metadata_non_cached(self, request_mock):
        request_mock.return_value = jsons.LATEST_METADATA
        self.assertEqual(self._api.get_latest_metadata(), jsons.LATEST_METADATA)
        self._api._request.assert_called_once_with(API_LATEST, jsonify=True)

    @patch.object(FFBinariesAPIClient, '_FFBinariesAPIClient__make_request', return_value={})
    def test_get_latest_metadata_cached(self, make_request_mock):
        with patch.object(self._api, '_use_caching', True), \
                patch.object(self._api._cache, '_cache',
                             {API_LATEST: (int(time.time()), jsons.LATEST_METADATA)}):
            self.assertEqual(self._api.get_latest_metadata(), jsons.LATEST_METADATA)
            self._api._FFBinariesAPIClient__make_request.assert_not_called()


if __name__ == '__main__':
    unittest.main()
