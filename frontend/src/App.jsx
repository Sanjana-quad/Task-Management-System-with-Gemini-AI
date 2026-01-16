import { useEffect, useState } from "react"
import {
  createTask,
  listTasks,
  startTask,
  completeTask,
  deleteTask,
} from "./api"
import { interpretCommand } from "./gemini"
import { dispatchAIIntent } from "./aiDispatcher"


export default function App() {
  const [tasks, setTasks] = useState([])
  const [title, setTitle] = useState("")
  const [filter, setFilter] = useState("")
  const [aiInput, setAiInput] = useState("")
const [aiError, setAiError] = useState("")


  async function loadTasks() {
    const data = await listTasks(filter || null)
    setTasks(data)
  }

  useEffect(() => {
    loadTasks()
  }, [filter])

  async function handleCreate(e) {
    e.preventDefault()
    if (!title) return
    await createTask(title)
    setTitle("")
    loadTasks()
  }

  async function handleStart(taskTitle) {
    await startTask(taskTitle)
    loadTasks()
  }

  async function handleComplete(taskTitle) {
    await completeTask(taskTitle)
    loadTasks()
  }

  async function handleDelete(taskTitle) {
    await deleteTask(taskTitle)
    loadTasks()
  }

  async function handleAICommand(e) {
  e.preventDefault()
  setAiError("")
  try {
    const intent = await interpretCommand(aiInput)
    console.log("AI intent:", intent)
    await dispatchAIIntent(intent)
    setAiInput("")
    loadTasks()
    
  } catch (err) {
    setAiError(err.message || "AI command failed")
  }
}


  return (
    <div style={{ padding: "2rem", maxWidth: "600px", margin: "auto" }}>
      <h2>Task Management System</h2>

      <form onSubmit={handleCreate}>
        <input
          placeholder="New task title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <button type="submit">Add</button>
      </form>

      <hr />

<h3>AI Assistant</h3>

<form onSubmit={handleAICommand} >
  <input
    placeholder="Ask AI (e.g. 'Start presentation task')"
    value={aiInput}
    onChange={(e) => setAiInput(e.target.value)}
    style={{ width: "100%" }}
    
  />
  <button type="submit">Send</button>
</form>

{aiError && <p style={{ color: "red" }}>{aiError}</p>}

      <div style={{ marginTop: "1rem" }}>
        <label>Filter:</label>
        <select onChange={(e) => setFilter(e.target.value)}>
          <option value="">All</option>
          <option value="Not Started">Not Started</option>
          <option value="In Progress">In Progress</option>
          <option value="Completed">Completed</option>
        </select>
      </div>

      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <strong>{task.title}</strong> — {task.state}

            {task.state === "Not Started" && (
              <button onClick={() => handleStart(task.title)}>Start</button>
            )}

            {task.state === "In Progress" && (
              <button onClick={() => handleComplete(task.title)}>
                Complete
              </button>
            )}

            <button onClick={() => handleDelete(task.title)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  )
}
