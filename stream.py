import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

data = {
    "model": "openai/gpt-4o-mini",
    "stream": True,
    "messages": [
        {
            "role": "user",
            "content": "Розкажи 5 смішних анекдотів про програмістів українською мовою."
        }
    ]
}

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    data=json.dumps(data),
    stream=True
)

for line in response.iter_lines():
    if not line:
        continue

    if line.startswith(b"data: "):
        decoded_line = line.decode("utf-8")[6:]
        if decoded_line.strip() == "[DONE]":
            break
        try:
            chunk = json.loads(decoded_line)
            delta = chunk["choices"][0]["delta"].get("content", "")
            print(delta, end="", flush=True)
        except json.JSONDecodeError:
            continue
