from django.urls import path
from tasks.api_views import (
    TaskCreateView,
    TaskListView,
    TaskStartView,
    TaskCompleteView,
    TaskDeleteView,
)

urlpatterns = [
    path("tasks", TaskCreateView.as_view()),
    path("tasks/list", TaskListView.as_view()),
    path("tasks/start", TaskStartView.as_view()),
    path("tasks/complete", TaskCompleteView.as_view()),
    path("tasks/delete", TaskDeleteView.as_view()),
]
