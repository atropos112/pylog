import logging


def str_to_logger_type(level: str) -> int:
    match level.lower():
        case "debug":
            return logging.DEBUG
        case "info":
            return logging.INFO
        case "warning":
            return logging.WARNING
        case "error":
            return logging.ERROR
        case "critical":
            return logging.CRITICAL
        case _:
            raise Exception(f"Unknown logger level: {level}")
