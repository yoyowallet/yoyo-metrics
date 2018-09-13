from typing import List, Optional

from datadog import DogStatsd

from .base import BaseMetricsBackend


def _prepare_tags(instance: Optional[str], tags: Optional[List[str]]) -> List[str]:
    if tags is None:
        tags = []
    if instance:
        tags += ['instance:{}'.format(instance)]
    return tags


class DatadogMetricsBackend(BaseMetricsBackend):
    def __init__(self, host: str, port:int, namespace:str):
        self.stats = DogStatsd(
            host=host,
            port=port,
            namespace=namespace,
        )

    def _gauge(self, metric, value, instance=None, tags=None, sample_rate=1):
        self.stats.gauge(
            metric=metric,
            value=value,
            tags=_prepare_tags(instance=instance, tags=tags),
            sample_rate=sample_rate,
        )

    def _increment(self, metric, value=1, instance=None, tags=None, sample_rate=1):
        self.stats.increment(
            metric=metric,
            value=value,
            tags=_prepare_tags(instance=instance, tags=tags),
            sample_rate=sample_rate,
        )

    def _timing(self, metric, value, instance=None, tags=None, sample_rate=1):
        self.stats.timing(
            metric=metric,
            value=value,
            tags=_prepare_tags(instance=instance, tags=tags),
            sample_rate=sample_rate,
        )
