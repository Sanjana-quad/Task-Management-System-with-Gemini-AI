const API_BASE = "http://127.0.0.1:8000/api"

export async function createTask(title) {
  const res = await fetch(`${API_BASE}/tasks`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  })
  return res.json()
}

export async function listTasks(state = null) {
  const url = state
    ? `${API_BASE}/tasks/list?state=${state}`
    : `${API_BASE}/tasks/list`

  const res = await fetch(url)
  return res.json()
}

export async function startTask(title) {
  const res = await fetch(`${API_BASE}/tasks/start`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  })
  return res.json()
}

export async function completeTask(title) {
  const res = await fetch(`${API_BASE}/tasks/complete`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  })
  return res.json()
}

export async function deleteTask(title) {
  await fetch(`${API_BASE}/tasks/delete`, {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  })
}
