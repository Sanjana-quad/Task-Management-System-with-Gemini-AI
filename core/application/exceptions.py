class ApplicationError(Exception):
    """Base class for all application-level errors."""
    pass


class TaskNotFound(ApplicationError):
    def __init__(self, identifier: str):
        super().__init__(f"No task found matching '{identifier}'.")


class MultipleTasksFound(ApplicationError):
    def __init__(self, identifier: str):
        super().__init__(
            f"Multiple tasks found matching '{identifier}'. Please be more specific."
        )
