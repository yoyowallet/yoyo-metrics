# Yoyo Metrics
This library exposes different backends to send metrics from Yoyo projects.

# Supported backends
## DummyBackend
This backend simply does nothing. Useful for testing.

## LoggingBackend
This backend shows metrics using a logger. Useful for debugging and testing.

## DatadogBackend
This backend sends metrics to Datadog. For this, it requires to be initialised with Datadog credentials.
