import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

messages = []

def send_message(message, messages):
    messages.append({"role": "user", "content": message})
    payload = {
        "model": "llama-3.1-8b-instant",
        "max_tokens": 1024,
        "messages": messages
    }
    r = requests.post(url, headers=headers, json=payload)
    if r.status_code == 200:
        data = r.json()
        print(data["choices"][0]["message"]["content"])
        messages.append({
            "role": "assistant",
            "content": data["choices"][0]["message"]["content"]
        })
    else:
        print("Error:", r.status_code)
        print(r.text)
    return messages

while True:
    message = input("You: ")
    if message.lower() == "exit":
        print("Goodbye")
        break
    else:
        messages = send_message(message, messages)