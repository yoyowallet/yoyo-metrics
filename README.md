# Yoyo Metrics
This library exposes different backends to send metrics from Yoyo projects.

# Supported backends
## BaseMetricsBackend
Base abstract class for creating new backends.

## DummyMetricsBackend
This backend simply does nothing. Useful for testing.

## LoggingMetricsBackend
This backend shows metrics using a logger. Useful for debugging and testing.

## DatadogMetricsBackend
This backend sends metrics to Datadog. For this, it requires to be initialised with Datadog credentials.

# Requirements
* Python 3+
