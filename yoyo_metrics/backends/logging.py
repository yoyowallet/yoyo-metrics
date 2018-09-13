from .base import BaseMetricsBackend


class LoggingMetricsBackend(BaseMetricsBackend):
    def __init__(self, logger) -> None:
        super().__init__()
        self.logger = logger

    def _gauge(self, metric, value, instance=None, tags=None, sample_rate=1):
        self.logger.debug(
            '%r: %+f', metric, value, extra={
                'instance': instance,
                'tags': tags or [],
            }
        )

    def _increment(self, metric, value=1, instance=None, tags=None, sample_rate=1):
        self.logger.debug(
            '%r: %+f', metric, value, extra={
                'instance': instance,
                'tags': tags or [],
            }
        )

    def _timing(self, metric, value, instance=None, tags=None, sample_rate=1):
        duration = 1000 * value
        self.logger.debug(
            '%r: %f ms', metric, duration, extra={
                'instance': instance,
                'tags': tags or [],
            }
        )
