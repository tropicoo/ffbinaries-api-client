FFBinaries API Client 
=====================
HTTP API Client for downloading pre-built ffmpeg, ffplay, ffprobe and ffserver packages.

* Contains optional caching mechanism for ffbinaries.com jsonified responses
* Supported components: `ffmpeg`, `ffplay`, `ffprobe` and `ffserver`
* Supported platforms: `linux-32`, `linux-64`, `linux-arm64`, `linux-armel`, `linux-armhf`, `osx-64`, `windows-32` and `windows-64`
* Supports fetching different versions of published components packages

Requirements
------------
Python 3+.
> Tested on Python 3.8 but any version of Python 3 should work
 
Installation
------------
```bash
pip3 install ffbinaries-api-client
```

Usage
-----
Public methods

```python
from ffbinaries import FFBinariesAPIClient

# API client can optionally cache ffbinaries.com json response with defined cache age in seconds.
# By default caching is turned off; Default cache age time is 300 seconds.
client = FFBinariesAPIClient(use_caching=True, cache_age=60)

client.get_latest_version()
client.get_latest_metadata()
client.get_available_versions()
client.get_available_versions_metadata()
client.get_exact_version_metadata('3.3')
client.download_latest_version('ffmpeg', 'windows-64', stream=True)
client.download_exact_version('ffmpeg', '3.3', 'windows-64', stream=True)
client.show_cache()
```

Examples located in `examples` directory.

Exception Handling
------------------
* `FFBinariesAPIClientError` is raised if something went wrong with API request.
* `InvalidArgumentError` is raised if `cache_age` arg won't be `float/int` 
type or less-equal than `0`.
* `NoCacheDataError` is raised when cache doesn't contain queried data
Currently handled internally and shouldn't be thrown up by API Client
* `ExpiredCacheDataError` is raised when cached URL data expired
* `CacheError` is base cache error, previous two inherit from it.

```python
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
```

Third Party Libraries and Dependencies
--------------------------------------
The following libraries will be installed when you install the client library:

* [requests](https://3.python-requests.org)
