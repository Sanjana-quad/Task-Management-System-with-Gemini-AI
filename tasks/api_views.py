from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.application.task_service import TaskService
from core.application.django_repository import DjangoTaskRepository
from core.application.exceptions import ApplicationError
from core.domain.exceptions import DomainError
from core.domain.task import TaskState


def get_task_service():
    return TaskService(DjangoTaskRepository())

class TaskCreateView(APIView):

    def post(self, request):
        title = request.data.get("title")

        if not title:
            return Response(
                {"error": "title is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        service = get_task_service()
        task = service.create_task(title)

        return Response(
            {
                "id": str(task.id),
                "title": task.title,
                "state": task.state.value,
            },
            status=status.HTTP_201_CREATED,
        )

class TaskListView(APIView):

    def get(self, request):
        state_param = request.query_params.get("state")
        service = get_task_service()

        try:
            state = TaskState(state_param) if state_param else None
        except ValueError:
            return Response(
                {"error": "Invalid state filter"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        tasks = service.list_tasks(state)

        return Response(
            [
                {
                    "id": str(task.id),
                    "title": task.title,
                    "state": task.state.value,
                }
                for task in tasks
            ],
            status=status.HTTP_200_OK,
        )

class TaskStartView(APIView):

    def post(self, request):
        title = request.data.get("title")

        if not title:
            return Response(
                {"error": "title is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        service = get_task_service()

        try:
            task = service.start_task(title)
            return Response(
                {
                    "id": str(task.id),
                    "title": task.title,
                    "state": task.state.value,
                },
                status=status.HTTP_200_OK,
            )

        except (ApplicationError, DomainError) as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

class TaskCompleteView(APIView):

    def post(self, request):
        title = request.data.get("title")

        if not title:
            return Response(
                {"error": "title is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        service = get_task_service()

        try:
            task = service.complete_task(title)
            return Response(
                {
                    "id": str(task.id),
                    "title": task.title,
                    "state": task.state.value,
                },
                status=status.HTTP_200_OK,
            )

        except (ApplicationError, DomainError) as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

class TaskDeleteView(APIView):

    def delete(self, request):
        title = request.data.get("title")

        if not title:
            return Response(
                {"error": "title is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        service = get_task_service()

        try:
            service.delete_task(title)
            return Response(status=status.HTTP_204_NO_CONTENT)

        except ApplicationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
