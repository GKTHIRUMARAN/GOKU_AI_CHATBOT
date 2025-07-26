import requests
import os

API_KEY = "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"  # ← Replace this with your actual key

MEMORY_FILE = "memory_log.txt"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def save_to_memory(user, assistant):
    with open(MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"User: {user}\\nGoku: {assistant}\\n")


def get_response(user_input):
    system_prompt = open("prompt.txt", "r", encoding="utf-8").read()
    memory = load_memory()

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "assistant", "content": f"{memory}"},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.8,
        "max_tokens": 500,
        "stream": False
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
    reply = response.json()["choices"][0]["message"]["content"]

    save_to_memory(user_input, reply)

    return reply