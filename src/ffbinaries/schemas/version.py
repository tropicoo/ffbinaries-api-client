from pydantic import BaseModel, Field

from ffbinaries.enums import PlatformCodeType


class ComponentSchema(BaseModel):
    ffmpeg: str | None = Field(
        default=None,
        description='FFmpeg binary ZIP archive URL',
        examples=[
            'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffmpeg-6.1-win-64.zip'
        ],
    )
    ffplay: str | None = Field(
        default=None,
        description='FFplay binary ZIP archive URL',
        examples=[
            'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffplay-6.1-win-64.zip'
        ],
    )
    ffprobe: str | None = Field(
        default=None,
        description='FFprobe binary ZIP archive URL',
        examples=[
            'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffprobe-6.1-win-64.zip'
        ],
    )
    ffserver: str | None = Field(
        default=None,
        description='FFserver binary ZIP archive URL',
        examples=[
            'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v6.1/ffserver-6.1-win-64.zip'
        ],
    )


class Windows32Schema(ComponentSchema):
    pass


class Windows64Schema(ComponentSchema):
    pass


class Linux32Schema(ComponentSchema):
    pass


class Linux64Schema(ComponentSchema):
    pass


class LinuxArmhfSchema(ComponentSchema):
    pass


class LinuxArmelSchema(ComponentSchema):
    pass


class LinuxArm64Schema(ComponentSchema):
    pass


class Osx64Schema(ComponentSchema):
    pass


class BinSchema(BaseModel):
    windows_32: Windows32Schema | None = Field(
        default=None,
        alias=PlatformCodeType.WIN32,
        description='Windows 32-bit binaries',
    )
    windows_64: Windows64Schema | None = Field(
        default=None,
        alias=PlatformCodeType.WIN64,
        description='Windows 64-bit binaries',
    )
    linux_32: Linux32Schema | None = Field(
        default=None,
        alias=PlatformCodeType.LINUX32,
        description='Linux 32-bit binaries',
    )
    linux_64: Linux64Schema | None = Field(
        default=None,
        alias=PlatformCodeType.LINUX64,
        description='Linux 64-bit binaries',
    )
    linux_armhf: LinuxArmhfSchema | None = Field(
        default=None,
        alias=PlatformCodeType.LINUX_ARMHF,
        description='Linux ARMHF binaries',
    )
    linux_armel: LinuxArmelSchema | None = Field(
        default=None,
        alias=PlatformCodeType.LINUX_ARMEL,
        description='Linux ARMEL binaries',
    )
    linux_arm64: LinuxArm64Schema | None = Field(
        default=None,
        alias=PlatformCodeType.LINUX_ARM64,
        description='Linux ARM64 binaries',
    )
    osx_64: Osx64Schema | None = Field(
        default=None, alias=PlatformCodeType.OSX64, description='OSX 64-bit binaries'
    )


class VersionResponseSchema(BaseModel):
    version: str = Field(description='Version of the FFmpeg binaries', examples=['6.1'])
    permalink: str = Field(
        description='Permalink to the current FFmpeg binaries version',
        examples=['https://ffbinaries.com/api/v1/version/6.1'],
    )
    bin: BinSchema = Field(description='FFmpeg binaries for different platforms')


class VersionsResponseSchema(BaseModel):
    versions: dict[str, str]
