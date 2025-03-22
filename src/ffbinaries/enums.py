__all__ = ['APIVersionType', 'ComponentType', 'HTTPMethodType', 'PlatformCodeType']


from enum import StrEnum
from typing import cast


class BaseStrChoiceEnum(StrEnum):
    @classmethod
    def choices(cls) -> tuple[str, ...]:
        return tuple(cast('str', x.value) for x in cls)


class HTTPMethodType(BaseStrChoiceEnum):
    DELETE = 'DELETE'
    GET = 'GET'
    HEAD = 'HEAD'
    OPTIONS = 'OPTIONS'
    PATCH = 'PATCH'
    POST = 'POST'
    PUT = 'PUT'


class APIVersionType(BaseStrChoiceEnum):
    V1 = 'v1'


class PlatformCodeType(BaseStrChoiceEnum):
    WIN32 = 'windows-32'
    WIN64 = 'windows-64'
    LINUX32 = 'linux-32'
    LINUX64 = 'linux-64'
    LINUX_ARMHF = 'linux-armhf'
    LINUX_ARMEL = 'linux-armel'
    LINUX_ARM64 = 'linux-arm64'
    OSX64 = 'osx-64'


class ComponentType(BaseStrChoiceEnum):
    FFMPEG = 'ffmpeg'
    FFPLAY = 'ffplay'
    FFPROBE = 'ffprobe'
    FFSERVER = 'ffserver'
