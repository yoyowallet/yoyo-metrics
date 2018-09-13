import logging

from .base import BaseMetricsBackend

logger = logging.getLogger(__name__)


class LoggingMetricsBackend(BaseMetricsBackend):
    def _gauge(self, metric, value, instance=None, tags=None, sample_rate=1):
        logger.debug(
            '%r: %+f', metric, value, extra={
                'instance': instance,
                'tags': tags or [],
            }
        )

    def _increment(self, metric, value=1, instance=None, tags=None, sample_rate=1):
        logger.debug(
            '%r: %+f', metric, value, extra={
                'instance': instance,
                'tags': tags or [],
            }
        )

    def _timing(self, metric, value, instance=None, tags=None, sample_rate=1):
        duration = 1000 * value
        logger.debug(
            '%r: %f ms', metric, duration, extra={
                'instance': instance,
                'tags': tags or [],
            }
        )
