from typing import Dict, List
from uuid import UUID

from core.application.repository import TaskRepository
from core.domain.task import Task


class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self._tasks: Dict[UUID, Task] = {}

    def save(self, task: Task) -> None:
        self._tasks[task.id] = task

    def get_by_id(self, task_id: UUID) -> Task | None:
        return self._tasks.get(task_id)

    def find_by_title(self, title: str) -> List[Task]:
        return [
            task for task in self._tasks.values()
            if task.title.lower() == title.lower()
        ]

    def list_all(self) -> List[Task]:
        return list(self._tasks.values())

    def delete(self, task_id: UUID) -> None:
        self._tasks.pop(task_id, None)
