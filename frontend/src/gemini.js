const GEMINI_API_KEY = import.meta.env.VITE_GEMINI_API_KEY

// ✅ MUST be defined before use
const GEMINI_ENDPOINT =
  "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"

function extractJSON(rawText) {
  return rawText
    .replace(/```json/gi, "")
    .replace(/```/g, "")
    .trim()
}

export async function interpretCommand(userText) {
  const prompt = `
You are an intent parser for a task management system.

IMPORTANT RULES:
- Only return START_TASK, COMPLETE_TASK, or DELETE_TASK
  if the user explicitly mentions a task name
- Use the FULL task title exactly as written by the user
- If the task title is ambiguous or unclear, set "title" to null
- If title is null, do NOT guess


Valid actions:
- CREATE_TASK
- START_TASK
- COMPLETE_TASK
- DELETE_TASK
- LIST_TASKS

Valid states:
- Not Started
- In Progress
- Completed

Return ONLY valid JSON.
No markdown. No explanation. No extra text.

JSON format:
{
  "action": "<ACTION>",
  "title": "<exact task title or null>",
  "state": "<state or null>"
}

User command:
"${userText}"
`

  const response = await fetch(
    `${GEMINI_ENDPOINT}?key=${GEMINI_API_KEY}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        contents: [
          {
            parts: [{ text: prompt }],
          },
        ],
      }),
    }
  )

  if (!response.ok) {
    const errorText = await response.text()
    throw new Error("Gemini API error: " + errorText)
  }

  const data = await response.json()

  const text =
    data?.candidates?.[0]?.content?.parts?.[0]?.text

  if (!text) {
    throw new Error("Invalid Gemini response format")
  }

  // 🔒 Treat AI output as untrusted input
  const cleaned = extractJSON(text)

  return JSON.parse(cleaned)
}
