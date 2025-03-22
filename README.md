FFBinaries API Client 
=====================
HTTP API Client for downloading pre-built ffmpeg, ffplay, ffprobe and ffserver packages from [FFbinaries](https://ffbinaries.com/).

* Supported components: `ffmpeg`, `ffplay`, `ffprobe` and `ffserver`
* Supported platforms: `linux-32`, `linux-64`, `linux-arm64`, `linux-armel`, `linux-armhf`, `osx-64`, `windows-32` and `windows-64`
* Supports fetching different versions of published components packages

Requirements
------------
Python 3.11+
 
Installation
------------
```bash
pip3 install ffbinaries-api-client
```

Usage
-----
V1 API client's public methods:

```python
from ffbinaries import FFBinariesV1APIClient, ComponentType, PlatformCodeType

client = FFBinariesV1APIClient(request_timeout=10)

client.get_latest_version()
client.get_latest_metadata()
client.get_available_versions()
client.get_available_versions_metadata()
client.get_exact_version_metadata(version='6.1')
client.download_latest_version(
    component=ComponentType.FFMPEG,
    platform=PlatformCodeType.WIN64,
    stream=True
)
client.download_exact_version(
    component=ComponentType.FFMPEG,
    version='6.1',
    platform=PlatformCodeType.WIN64,
    stream=True,
)

```

Examples located in `examples` directory.

Exception Handling
------------------
* `FFBinariesAPIClientError` is raised if something went wrong with API request.

```python
class FFBinariesAPIClientError(Exception):
    """General API Client Error Class."""
    pass
```

Third Party Libraries and Dependencies
--------------------------------------
The following libraries will be installed when you install the client library:

* [Requests](https://requests.readthedocs.io/en/latest/)
* [Pydantic](https://docs.pydantic.dev/latest/)
