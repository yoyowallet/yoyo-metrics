import logging
import threading
from abc import ABC, abstractmethod
from typing import Any, List, Optional

logger = logging.getLogger(__name__)


class BaseMetricsBackend(ABC, threading.local):
    def gauge(self, metric: str, value: Any, instance: str = None, tags: Optional[List[str]] = None,
              sample_rate: int = 1) -> None:
        """
        Record the current value of a metric, optionally setting an instance name and tags.

        :param metric: Metric name
        :param value: Current value of metric
        :param instance: Instance name
        :param tags: List of tags
        :param sample_rate:

        >>> gauge('user.count', 100000)
        """
        try:
            self._gauge(metric, value, instance=instance, tags=tags, sample_rate=sample_rate)
        except Exception:
            logger.exception('Unable to record metric')

    @abstractmethod
    def _gauge(self, metric: str, value: Any, instance: str = None, tags: Optional[List[str]] = None,
               sample_rate: int = 1) -> None:
        pass

    def increment(self, metric: str, value: int = 1, instance: str = None, tags: Optional[List[str]] = None,
                  sample_rate: int = 1) -> None:
        """
        Increment a counter, optionally setting an increment value (defaults to +1), an instance name and tags.

        :param metric: Metric name
        :param value: Increment amount
        :param instance: Instance name
        :param tags: List of tags
        :param sample_rate:

        >>> increment('page.views')
        >>> increment('files.transferred', 124)
        >>> increment('celery.started', instance='y2klogin.sync.health', tags=['result:success'])
        >>> increment('auth.success', tags=['kind:facebook'])
        """
        try:
            self._increment(metric, value, instance=instance, tags=tags, sample_rate=sample_rate)
        except Exception:
            logger.exception('Unable to record metric')

    @abstractmethod
    def _increment(self, metric: str, value: int = 1, instance: str = None, tags: Optional[List[str]] = None,
                   sample_rate: int = 1) -> None:
        pass

    def timing(self, metric: str, value: Any, instance: str = None, tags: Optional[List[str]] = None,
               sample_rate: int = 1) -> None:
        """
        Record a timing, optionally setting an instance name and tags.

        :param metric: Metric name
        :param value: Value in seconds
        :param str instance: Instance name
        :param list[str or unicode] tags: List of tags
        :param sample_rate

        >>> timing('query.response.time', 0.1)
        >>> timing('celery.runtime', 0.1, instance='y2klogin.sync.health', tags=['result:success'])
        """
        try:
            self._gauge(metric, value, instance=instance, tags=tags, sample_rate=sample_rate)
        except Exception:
            logger.exception('Unable to record metric')

    @abstractmethod
    def _timing(self, metric: str, value: Any, instance: str = None, tags: Optional[List[str]] = None,
                sample_rate: int = 1) -> None:
        pass
