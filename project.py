import requests
from dotenv import load_dotenv
import os
import json

# ── Setup ─────────────────────────────────────────────────────────────────────

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Groq API endpoint
url = "https://api.groq.com/openai/v1/chat/completions"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Stores full conversation history for multi-turn context
messages = []


# ── Functions ─────────────────────────────────────────────────────────────────

def send_message(message, messages):
    """Send user message to Groq API and get AI response."""

    # Add user message to history before sending
    messages.append({"role": "user", "content": message})

    # Build request payload
    payload = {
        "model": "llama-3.1-8b-instant",
        "max_tokens": 1024,
        "messages": messages  # full history sent for context
    }

    # Make POST request to Groq API
    r = requests.post(url, headers=headers, json=payload)

    if r.status_code == 200:
        data = r.json()
        response = data["choices"][0]["message"]["content"]

        # Print AI response
        print(f"Bot: {response}")

        # Add AI response to history
        messages.append({
            "role": "assistant",
            "content": response
        })
    else:
        print("Error:", r.status_code)
        print(r.text)

    return messages


def show_history(messages):
    """Display full conversation history."""
    if not messages:
        print("No history yet.")
    else:
        print("\n── Conversation History ──")
        for i, message in enumerate(messages, 1):
            print(f"{i}. {message['role']}: {message['content']}")
        print("─────────────────────────\n")


def clear_history(messages):
    """Clear all messages from conversation history."""
    if not messages:
        print("No history to clear.")
    else:
        messages.clear()
        print("History cleared!")


def save_conversation(messages):
    """Save current conversation to Conversation.json."""
    if not messages:
        print("No conversation to save.")
    else:
        with open("Conversation.json", "w") as f:
            json.dump(messages, f, indent=2)
        print("Conversation saved!")


def load_conversation():
    """Load a previously saved conversation from Conversation.json."""
    if os.path.exists("Conversation.json"):
        with open("Conversation.json", "r") as f:
            print("Conversation loaded!")
            return json.load(f)
    else:
        print("No saved conversation found.")
        return []


# ── Main Loop ─────────────────────────────────────────────────────────────────

print("── CLI Chatbot ──────────────────────────────")
print("Commands: show history | clear history |")
print("          save conversation | load conversation | exit")
print("─────────────────────────────────────────────\n")

while True:
    message = input("You: ")

    if message.lower() == "show history":
        show_history(messages)
    elif message.lower() == "clear history":
        clear_history(messages)
    elif message.lower() == "save conversation":
        save_conversation(messages)
    elif message.lower() == "load conversation":
        messages = load_conversation()
    elif message.lower() == "exit":
        print("Goodbye!")
        break
    else:
        messages = send_message(message, messages)