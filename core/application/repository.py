from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from core.domain.task import Task


class TaskRepository(ABC):

    @abstractmethod
    def save(self, task: Task) -> None:
        pass

    @abstractmethod
    def get_by_id(self, task_id: UUID) -> Task | None:
        pass

    @abstractmethod
    def find_by_title(self, title: str) -> List[Task]:
        pass

    @abstractmethod
    def list_all(self) -> List[Task]:
        pass

    @abstractmethod
    def delete(self, task_id: UUID) -> None:
        pass
