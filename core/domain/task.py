from enum import Enum
from uuid import UUID

from core.domain.exceptions import (
    InvalidStateTransition,
    TaskAlreadyCompleted,
)


class TaskState(str, Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


ALLOWED_STATE_TRANSITIONS = {
    TaskState.NOT_STARTED: {TaskState.IN_PROGRESS},
    TaskState.IN_PROGRESS: {TaskState.COMPLETED},
    TaskState.COMPLETED: set(),
}


class Task:
    def __init__(
        self,
        *,
        task_id: UUID,
        title: str,
        state: TaskState = TaskState.NOT_STARTED,
    ):
        self.id = task_id
        self.title = title
        self._state = state

    @property
    def state(self) -> TaskState:
        return self._state

    def _transition_to(self, new_state: TaskState) -> None:
        if self._state == TaskState.COMPLETED:
            raise TaskAlreadyCompleted()

        allowed = ALLOWED_STATE_TRANSITIONS[self._state]
        if new_state not in allowed:
            raise InvalidStateTransition(self._state, new_state)

        self._state = new_state

    def start(self) -> None:
        self._transition_to(TaskState.IN_PROGRESS)

    def complete(self) -> None:
        self._transition_to(TaskState.COMPLETED)
