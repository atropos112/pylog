from pydantic import BaseSettings

from pylog.logger_type import LoggerType


class BaseLoggerSettings(BaseSettings):
    type: str | None | LoggerType = None
    level: str | int | None = None

    class Config:
        env_prefix = "ATRO_PYLOG_"
        env_file = ".env"
        env_file_encoding = "utf-8"


class OpenTelemetryLoggerSettings(BaseSettings):
    service_name: str | None = __name__
    instance_id: str | None = __name__
    endpoint: str | None = None

    class Config:
        env_prefix = "ATRO_PYLOG_"
        env_file = ".env"
        env_file_encoding = "utf-8"


class LoguruLoggerSettings(BaseSettings):
    class Config:
        env_prefix = "ATRO_PYLOG_"
        env_file = ".env"
        env_file_encoding = "utf-8"
