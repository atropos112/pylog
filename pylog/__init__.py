import logging
import sys
from pathlib import Path

sys.path.append(Path(__file__).resolve().parent.parent.as_posix())

from pylog.logger_type import LoggerType  # noqa E402
from pylog.opentelemetry_setup import open_telemetry_logger_setup  # noqa E402
from pylog.rich_setup import rich_logger_setup  # noqa E402
from pylog.settings import BaseLoggerSettings, OpenTelemetryLoggerSettings  # noqa E402


def get_logger(base_settings: BaseLoggerSettings = BaseLoggerSettings(), open_telemetry_settings: OpenTelemetryLoggerSettings = OpenTelemetryLoggerSettings()):
    logger = logging.getLogger(base_settings.name)

    match base_settings.type:
        case LoggerType.RICH:
            rich_logger_setup(base_settings)
        case LoggerType.OPENTELEMETRY:
            open_telemetry_logger_setup(base_settings, open_telemetry_settings)
        case _:
            raise Exception(f"Unknown logger type: {type}")

    return logger
