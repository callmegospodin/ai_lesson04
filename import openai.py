import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
image_url = "https://kryivka.net/upload/iblock/214/2145ea5f5647d4213c762fb7de8b8442.jpg"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

data = {
    "model": "google/gemini-pro-vision",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "This image contains an English language test. "
                        "Please extract each question and only the correct answer for it. "
                        "Output format: \n\nQuestion: <question text>\nCorrect answer: <answer text>\n"
                    )
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                }
            ]
        }
    ]
}

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    data=json.dumps(data)
)

if response.status_code == 200:
    result = response.json()
    message = result['choices'][0]['message']['content']
    print(message)
else:
    print(f"Error: {response.status_code} - {response.text}")
