from pydantic import BaseModel, Field

from ffbinaries.enums import PlatformCodeType


class ComponentSchema(BaseModel):
    ffmpeg: str | None = None
    ffplay: str | None = None
    ffprobe: str | None = None
    ffserver: str | None = None


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
        default=None, alias=PlatformCodeType.WIN32
    )
    windows_64: Windows64Schema | None = Field(
        default=None, alias=PlatformCodeType.WIN64
    )
    linux_32: Linux32Schema | None = Field(default=None, alias=PlatformCodeType.LINUX32)
    linux_64: Linux64Schema | None = Field(default=None, alias=PlatformCodeType.LINUX64)
    linux_armhf: LinuxArmhfSchema | None = Field(
        default=None, alias=PlatformCodeType.LINUX_ARMHF
    )
    linux_armel: LinuxArmelSchema | None = Field(
        default=None, alias=PlatformCodeType.LINUX_ARMEL
    )
    linux_arm64: LinuxArm64Schema | None = Field(
        default=None, alias=PlatformCodeType.LINUX_ARM64
    )
    osx_64: Osx64Schema | None = Field(default=None, alias=PlatformCodeType.OSX64)


class VersionResponseSchema(BaseModel):
    version: str
    permalink: str
    bin: BinSchema


class VersionsResponseSchema(BaseModel):
    versions: dict[str, str]
