import {
  createTask,
  startTask,
  completeTask,
  deleteTask,
  listTasks,
} from "./api"

export async function dispatchAIIntent(intent) {
  const { action, title, state } = intent

  switch (action) {
    case "CREATE_TASK":
        if (!title) throw new Error("Task title is required to create a task")
      return createTask(title)

    case "START_TASK":
       if (!title)
        throw new Error(
          "I couldn’t figure out which task to start. Please use the exact task name."
        )
      return startTask(title)

    case "COMPLETE_TASK":
        if (!title)
        throw new Error(
          "I couldn’t figure out which task to complete. Please use the exact task name."
        )
      return completeTask(title)

    case "DELETE_TASK":
        if (!title)
        throw new Error(
          "I couldn’t figure out which task to delete. Please use the exact task name."
        )
      return deleteTask(title)

    case "LIST_TASKS":
      return listTasks(state)

    default:
      throw new Error("Unsupported AI action")
  }
}
