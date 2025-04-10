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
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Згенеруй, будь ласка, 25 креативних ідей для стартапів у сфері ІТ. "
                        "Формат відповіді: номер ідеї, короткий опис, бажано українською мовою."
                    )
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
