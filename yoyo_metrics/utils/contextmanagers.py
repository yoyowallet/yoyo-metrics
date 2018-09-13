import time
from contextlib import contextmanager
from typing import Optional, List

from yoyo_metrics.backends.base import BaseMetricsBackend


@contextmanager
def timer(backend: BaseMetricsBackend, metric: str, instance: str = None, tags: Optional[List[str]] = None) -> None:
    """
    A context manager that will measure the distribution of a context's run time.
    Optionally setting an instance name and tags.

    :param backend: Metrics to backend to use for sending metric
    :param metric: Metric name
    :param instance: Instance name
    :param tags: List of tags

    >>> with timer('yoyowallet.runtime') as tags:
    >>>     tags += ['method:get', 'endpoint:accounts']
    >>>     requests.get('https://www.yoyowallet.com/api/accounts/7ddf32e17a6ac5ce04a8ecbf782ca509')
    """
    if tags is None:
        tags = []

    start = time.time()

    try:
        yield tags
    except Exception:
        tags += ['result:failure']
        raise
    else:
        tags += ['result:success']
    finally:
        duration = time.time() - start
        backend.timing(metric, duration, instance=instance, tags=tags)
