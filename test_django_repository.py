import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.application.task_service import TaskService
from core.application.django_repository import DjangoTaskRepository
from core.domain.task import TaskState


def run_tests():
    repo = DjangoTaskRepository()
    service = TaskService(repo)

    print("Creating task...")
    service.create_task("Prepare presentation")

    print("Starting task...")
    service.start_task("Prepare presentation")

    print("Completing task...")
    service.complete_task("Prepare presentation")

    print("\nCompleted tasks:")
    for task in service.list_tasks(TaskState.COMPLETED):
        print(task.title, task.state)


if __name__ == "__main__":
    run_tests()
