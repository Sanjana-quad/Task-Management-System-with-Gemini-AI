from uuid import uuid4
from typing import List

from core.domain.task import Task, TaskState
from core.application.repository import TaskRepository
from core.application.exceptions import (
    TaskNotFound,
    MultipleTasksFound,
)


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, title: str) -> Task:
        task = Task(
            task_id=uuid4(),
            title=title,
            state=TaskState.NOT_STARTED,
        )
        self.repository.save(task)
        return task

    def list_tasks(self, state: TaskState | None = None) -> List[Task]:
        tasks = self.repository.list_all()
        if state is None:
            return tasks
        return [task for task in tasks if task.state == state]

    def _resolve_single_task(self, identifier: str) -> Task:
        matches = self.repository.find_by_title(identifier)

        if not matches:
            raise TaskNotFound(identifier)

        if len(matches) > 1:
            raise MultipleTasksFound(identifier)

        return matches[0]

    def start_task(self, identifier: str) -> Task:
        task = self._resolve_single_task(identifier)
        task.start()
        self.repository.save(task)
        return task

    def complete_task(self, identifier: str) -> Task:
        task = self._resolve_single_task(identifier)
        task.complete()
        self.repository.save(task)
        return task

    def delete_task(self, identifier: str) -> None:
        task = self._resolve_single_task(identifier)
        self.repository.delete(task.id)
