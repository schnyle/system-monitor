import numpy as np
import psutil

from datetime import datetime
from dtypes import CPULoadMetrics
from monitor.base import BaseMonitor


class CPULoadMonitor(BaseMonitor[CPULoadMetrics]):
    def __init__(self) -> None:
        super().__init__()

    def _init_current_metrics(self) -> CPULoadMetrics:
        return CPULoadMetrics(timestamp=datetime.now(),
                              usage_total_percent=0.0, usage_percpu_percent=[])

    def _collect(self) -> None:
        result: list[float] = psutil.cpu_percent(interval=None, percpu=True)

        self.current_metrics.timestamp = datetime.now()
        self.current_metrics.usage_total_percent = np.average(
            result).astype(float)
        self.current_metrics.usage_percpu_percent = result
