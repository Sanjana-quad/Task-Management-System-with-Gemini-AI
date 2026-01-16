from typing import List
from uuid import UUID

from tasks.models import TaskModel
from core.domain.task import Task, TaskState
from core.application.repository import TaskRepository


class DjangoTaskRepository(TaskRepository):

    def save(self, task: Task) -> None:
        obj, _ = TaskModel.objects.update_or_create(
            id=task.id,
            defaults={
                "title": task.title,
                "state": task.state.value,
            },
        )

    def get_by_id(self, task_id: UUID) -> Task | None:
        try:
            obj = TaskModel.objects.get(id=task_id)
            return self._to_domain(obj)
        except TaskModel.DoesNotExist:
            return None

    def find_by_title(self, title: str) -> List[Task]:
        objs = TaskModel.objects.filter(title__iexact=title)
        return [self._to_domain(obj) for obj in objs]

    def list_all(self) -> List[Task]:
        return [self._to_domain(obj) for obj in TaskModel.objects.all()]

    def delete(self, task_id: UUID) -> None:
        TaskModel.objects.filter(id=task_id).delete()

    def _to_domain(self, obj: TaskModel) -> Task:
        return Task(
            task_id=obj.id,
            title=obj.title,
            state=TaskState(obj.state),
        )
