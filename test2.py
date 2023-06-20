import logging

from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource

logger_provider = LoggerProvider(
    resource=Resource.create(
        {
            "service.name": "shoppingcart",
            "service.instance.id": "instance-12",
        },
    ),
)
set_logger_provider(logger_provider)

exporter = OTLPLogExporter(insecure=True)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)

# Attach OTLP handler to root logger
logging.getLogger().addHandler(handler)

# Log directly
logging.info("directly info message")

# Create different namespaced loggers
logger1 = logging.getLogger("some.app")
logger1.setLevel(logging.DEBUG)
logger2 = logging.getLogger("myapp.area2")

logger1.debug("debug message")
logger1.info("info message")
# logger1.info("How quickly daft jumping zebras vex.")
# logger2.warning("Jail zesty vixen who grabbed pay from quack.")
# logger2.error("The five boxing wizards jump quickly.")


# # Trace context correlation
# tracer = trace.get_tracer(__name__)
# with tracer.start_as_current_span("foo"):
#     # Do something
#     logger2.error("Hyderabad, we have a major problem.")

logger_provider.shutdown()
