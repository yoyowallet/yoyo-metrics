from .base import BaseMetricsBackend


class DummyMetricsBackend(BaseMetricsBackend):
    def _gauge(self, metric, value, instance=None, tags=None, sample_rate=1):
        pass

    def _increment(self, metric, value=1, instance=None, tags=None, sample_rate=1):
        pass

    def _timing(self, metric, value, instance=None, tags=None, sample_rate=1):
        pass
