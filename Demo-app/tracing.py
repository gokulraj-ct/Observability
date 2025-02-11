from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc import OTLPSpanExporter
from opentelemetry.instrumentation.requests import RequestsInstrumentor

# Set up OpenTelemetry tracing
trace.set_tracer_provider(TracerProvider())

# Set up the OTLP exporter
otlp_exporter = OTLPSpanExporter(endpoint="http://otel-collector:4317", insecure=True)  # Replace with your OTLP endpoint
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Automatically instrument HTTP requests and other libraries as needed
RequestsInstrumentor().instrument()

print("OpenTelemetry Tracing is set up!")
