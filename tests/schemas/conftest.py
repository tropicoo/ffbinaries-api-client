from typing import Final

from pydantic import BaseModel

from ffbinaries import PlatformCodeType
from ffbinaries.schemas.version import (
    BaseComponentSchema,
    BinSchema,
    Linux32Schema,
    Linux64Schema,
    LinuxArm64Schema,
    LinuxArmelSchema,
    LinuxArmhfSchema,
    Osx64Schema,
    VersionResponseSchema,
    VersionsResponseSchema,
    Windows32Schema,
    Windows64Schema,
)

BASE_COMPONENT_SCHEMA_JSON_SCHEMA: Final[dict] = {
    'properties': {
        'ffmpeg': {
            'anyOf': [{'type': 'string'}, {'type': 'null'}],
            'default': None,
            'description': 'FFmpeg binary ZIP archive URL',
            'examples': [
                'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffmpeg-6.1-win-64.zip'
            ],
            'title': 'Ffmpeg',
        },
        'ffplay': {
            'anyOf': [{'type': 'string'}, {'type': 'null'}],
            'default': None,
            'description': 'FFplay binary ZIP archive URL',
            'examples': [
                'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffplay-6.1-win-64.zip'
            ],
            'title': 'Ffplay',
        },
        'ffprobe': {
            'anyOf': [{'type': 'string'}, {'type': 'null'}],
            'default': None,
            'description': 'FFprobe binary ZIP archive URL',
            'examples': [
                'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffprobe-6.1-win-64.zip'
            ],
            'title': 'Ffprobe',
        },
        'ffserver': {
            'anyOf': [{'type': 'string'}, {'type': 'null'}],
            'default': None,
            'description': 'FFserver binary ZIP archive URL',
            'examples': [
                'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffserver-6.1-win-64.zip'
            ],
            'title': 'Ffserver',
        },
    },
    'title': 'BaseComponentSchema',
    'type': 'object',
}


BIN_SCHEMA_JSON_SCHEMA: Final[dict] = {
    '$defs': {
        'Linux32Schema': {
            'properties': {
                'ffmpeg': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFmpeg binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffmpeg-6.1-win-64.zip'
                    ],
                    'title': 'Ffmpeg',
                },
                'ffplay': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFplay binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffplay-6.1-win-64.zip'
                    ],
                    'title': 'Ffplay',
                },
                'ffprobe': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFprobe binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffprobe-6.1-win-64.zip'
                    ],
                    'title': 'Ffprobe',
                },
                'ffserver': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFserver binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffserver-6.1-win-64.zip'
                    ],
                    'title': 'Ffserver',
                },
            },
            'title': 'Linux32Schema',
            'type': 'object',
        },
        'Linux64Schema': {
            'properties': {
                'ffmpeg': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFmpeg binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffmpeg-6.1-win-64.zip'
                    ],
                    'title': 'Ffmpeg',
                },
                'ffplay': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFplay binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffplay-6.1-win-64.zip'
                    ],
                    'title': 'Ffplay',
                },
                'ffprobe': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFprobe binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffprobe-6.1-win-64.zip'
                    ],
                    'title': 'Ffprobe',
                },
                'ffserver': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFserver binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffserver-6.1-win-64.zip'
                    ],
                    'title': 'Ffserver',
                },
            },
            'title': 'Linux64Schema',
            'type': 'object',
        },
        'LinuxArm64Schema': {
            'properties': {
                'ffmpeg': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFmpeg binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffmpeg-6.1-win-64.zip'
                    ],
                    'title': 'Ffmpeg',
                },
                'ffplay': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFplay binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffplay-6.1-win-64.zip'
                    ],
                    'title': 'Ffplay',
                },
                'ffprobe': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFprobe binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffprobe-6.1-win-64.zip'
                    ],
                    'title': 'Ffprobe',
                },
                'ffserver': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFserver binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffserver-6.1-win-64.zip'
                    ],
                    'title': 'Ffserver',
                },
            },
            'title': 'LinuxArm64Schema',
            'type': 'object',
        },
        'LinuxArmelSchema': {
            'properties': {
                'ffmpeg': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFmpeg binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffmpeg-6.1-win-64.zip'
                    ],
                    'title': 'Ffmpeg',
                },
                'ffplay': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFplay binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffplay-6.1-win-64.zip'
                    ],
                    'title': 'Ffplay',
                },
                'ffprobe': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFprobe binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffprobe-6.1-win-64.zip'
                    ],
                    'title': 'Ffprobe',
                },
                'ffserver': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFserver binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffserver-6.1-win-64.zip'
                    ],
                    'title': 'Ffserver',
                },
            },
            'title': 'LinuxArmelSchema',
            'type': 'object',
        },
        'LinuxArmhfSchema': {
            'properties': {
                'ffmpeg': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFmpeg binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffmpeg-6.1-win-64.zip'
                    ],
                    'title': 'Ffmpeg',
                },
                'ffplay': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFplay binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffplay-6.1-win-64.zip'
                    ],
                    'title': 'Ffplay',
                },
                'ffprobe': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFprobe binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffprobe-6.1-win-64.zip'
                    ],
                    'title': 'Ffprobe',
                },
                'ffserver': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFserver binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffserver-6.1-win-64.zip'
                    ],
                    'title': 'Ffserver',
                },
            },
            'title': 'LinuxArmhfSchema',
            'type': 'object',
        },
        'Osx64Schema': {
            'properties': {
                'ffmpeg': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFmpeg binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffmpeg-6.1-win-64.zip'
                    ],
                    'title': 'Ffmpeg',
                },
                'ffplay': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFplay binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffplay-6.1-win-64.zip'
                    ],
                    'title': 'Ffplay',
                },
                'ffprobe': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFprobe binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffprobe-6.1-win-64.zip'
                    ],
                    'title': 'Ffprobe',
                },
                'ffserver': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFserver binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffserver-6.1-win-64.zip'
                    ],
                    'title': 'Ffserver',
                },
            },
            'title': 'Osx64Schema',
            'type': 'object',
        },
        'Windows32Schema': {
            'properties': {
                'ffmpeg': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFmpeg binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffmpeg-6.1-win-64.zip'
                    ],
                    'title': 'Ffmpeg',
                },
                'ffplay': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFplay binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffplay-6.1-win-64.zip'
                    ],
                    'title': 'Ffplay',
                },
                'ffprobe': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFprobe binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffprobe-6.1-win-64.zip'
                    ],
                    'title': 'Ffprobe',
                },
                'ffserver': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFserver binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffserver-6.1-win-64.zip'
                    ],
                    'title': 'Ffserver',
                },
            },
            'title': 'Windows32Schema',
            'type': 'object',
        },
        'Windows64Schema': {
            'properties': {
                'ffmpeg': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFmpeg binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffmpeg-6.1-win-64.zip'
                    ],
                    'title': 'Ffmpeg',
                },
                'ffplay': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFplay binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffplay-6.1-win-64.zip'
                    ],
                    'title': 'Ffplay',
                },
                'ffprobe': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFprobe binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffprobe-6.1-win-64.zip'
                    ],
                    'title': 'Ffprobe',
                },
                'ffserver': {
                    'anyOf': [{'type': 'string'}, {'type': 'null'}],
                    'default': None,
                    'description': 'FFserver binary ZIP archive URL',
                    'examples': [
                        'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffserver-6.1-win-64.zip'
                    ],
                    'title': 'Ffserver',
                },
            },
            'title': 'Windows64Schema',
            'type': 'object',
        },
    },
    'properties': {
        PlatformCodeType.WIN32: {
            'anyOf': [{'$ref': '#/$defs/Windows32Schema'}, {'type': 'null'}],
            'default': None,
            'description': 'Windows 32-bit binaries',
        },
        PlatformCodeType.WIN64: {
            'anyOf': [{'$ref': '#/$defs/Windows64Schema'}, {'type': 'null'}],
            'default': None,
            'description': 'Windows 64-bit binaries',
        },
        PlatformCodeType.LINUX32: {
            'anyOf': [{'$ref': '#/$defs/Linux32Schema'}, {'type': 'null'}],
            'default': None,
            'description': 'Linux 32-bit binaries',
        },
        PlatformCodeType.LINUX64: {
            'anyOf': [{'$ref': '#/$defs/Linux64Schema'}, {'type': 'null'}],
            'default': None,
            'description': 'Linux 64-bit binaries',
        },
        PlatformCodeType.LINUX_ARMHF: {
            'anyOf': [{'$ref': '#/$defs/LinuxArmhfSchema'}, {'type': 'null'}],
            'default': None,
            'description': 'Linux ARMHF binaries',
        },
        PlatformCodeType.LINUX_ARMEL: {
            'anyOf': [{'$ref': '#/$defs/LinuxArmelSchema'}, {'type': 'null'}],
            'default': None,
            'description': 'Linux ARMEL binaries',
        },
        PlatformCodeType.LINUX_ARM64: {
            'anyOf': [{'$ref': '#/$defs/LinuxArm64Schema'}, {'type': 'null'}],
            'default': None,
            'description': 'Linux ARM64 binaries',
        },
        PlatformCodeType.OSX64: {
            'anyOf': [{'$ref': '#/$defs/Osx64Schema'}, {'type': 'null'}],
            'default': None,
            'description': 'OSX 64-bit binaries',
        },
    },
    'title': 'BinSchema',
    'type': 'object',
}


VERSIONS_RESPONSE_SCHEMA_JSON_SCHEMA: Final[dict] = {
    'properties': {
        'versions': {
            'additionalProperties': {'type': 'string'},
            'title': 'Versions',
            'type': 'object',
        }
    },
    'required': ['versions'],
    'title': 'VersionsResponseSchema',
    'type': 'object',
}


PYDANTIC_COMPONENT_CLASSES: Final[tuple[type[BaseComponentSchema], ...]] = (
    BaseComponentSchema,
    Windows32Schema,
    Windows64Schema,
    Linux32Schema,
    Linux64Schema,
    LinuxArmhfSchema,
    LinuxArmelSchema,
    LinuxArm64Schema,
    Osx64Schema,
)
PYDANTIC_OTHER_SCHEMAS: Final[tuple[type[BaseModel], ...]] = (
    BinSchema,
    VersionResponseSchema,
    VersionsResponseSchema,
)


PYDANTIC_SCHEMAS: Final[tuple[type[BaseModel], ...]] = (
    *PYDANTIC_COMPONENT_CLASSES,
    *PYDANTIC_OTHER_SCHEMAS,
)
