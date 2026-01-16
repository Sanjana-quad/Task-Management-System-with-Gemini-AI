class DomainError(Exception):
    """Base class for all domain-level errors."""
    pass


class InvalidStateTransition(DomainError):
    def __init__(self, from_state: str, to_state: str):
        super().__init__(
            f"Invalid task state transition from '{from_state}' to '{to_state}'."
        )


class TaskAlreadyCompleted(DomainError):
    def __init__(self):
        super().__init__("Task is already completed and cannot be modified.")
