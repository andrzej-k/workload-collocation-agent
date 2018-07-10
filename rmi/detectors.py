from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod
from typing import List, Dict, Union

from rmi.metrics import Metric, MetricName
from rmi.mesos import TaskId
from rmi.platforms import Platform


# Mapping from metric type to specific value (unit depends on metric type)
TaskMetricValues = Dict[MetricName, Union[float, int]]
TasksMetricValues = Dict[TaskId, TaskMetricValues]


class ContendedResource(Enum):

    MEMORY = 'memory bandwidth'
    LLC = 'cache'
    CPUS = 'cpus'


@dataclass
class Anomaly:

    task_ids: List[TaskId]
    resource: ContendedResource


class AnomalyDectector(ABC):

    @abstractmethod
    def detect(
            self,
            platform: Platform,
            tasks_metric_values: TasksMetricValues) -> (List[Anomaly], List[Metric]):
        ...


class NOPAnomalyDectector(AnomalyDectector):

    def detect(self, platform, tasks_metric_values):
        return [], []
