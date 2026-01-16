from core.application.task_service import TaskService
from core.application.in_memory_repository import InMemoryTaskRepository
from core.application.exceptions import ApplicationError
from core.domain.exceptions import DomainError
from core.domain.task import TaskState


def run_tests():
    repo = InMemoryTaskRepository()
    service = TaskService(repo)

    print("\nCreating tasks...")
    service.create_task("Prepare presentation")
    service.create_task("Write report")

    print("\nListing all tasks:")
    for task in service.list_tasks():
        print(task.title, "-", task.state)

    print("\nStarting 'Prepare presentation'...")
    service.start_task("Prepare presentation")

    print("\nCompleting 'Prepare presentation'...")
    service.complete_task("Prepare presentation")

    print("\nListing completed tasks:")
    for task in service.list_tasks(TaskState.COMPLETED):
        print(task.title, "-", task.state)

    print("\nTrying to start completed task (should fail):")
    try:
        service.start_task("Prepare presentation")
    except DomainError as e:
        print("Caught domain error:", e)

    print("\nTrying unknown task (should fail):")
    try:
        service.start_task("Nonexistent task")
    except ApplicationError as e:
        print("Caught application error:", e)


if __name__ == "__main__":
    run_tests()
