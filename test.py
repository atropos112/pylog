from time import sleep

from pylog import get_logger

logger = get_logger(type="opentelemetry", endpoint="http://127.0.0.1:4317", service_name="jacek", service_instance_id="jacek-instance")
while True:
    logger.info("Hello World!")
    sleep(2)
