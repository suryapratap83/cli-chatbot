# CLI Chatbot 🤖

A command-line chatbot built in Python using the Groq API. Supports multi-turn conversations with save and load functionality.

## Features
- Chat with an AI in your terminal
- Multi-turn conversation (remembers context)
- Show conversation history
- Clear conversation history
- Save conversation to a JSON file
- Load previously saved conversation

## Setup

1. Clone the repo
2. Create a virtual environment:
   python -m venv venv
   venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
4. Create a .env file and add your Groq API key:
   GROQ_API_KEY=your-key-here
5. Run:
   python chatbot.py

## Commands
| Command | Description |
|---------|-------------|
| Any message | Chat with the AI |
| `show history` | View full conversation history |
| `clear history` | Clear conversation history |
| `save conversation` | Save conversation to JSON file |
| `load conversation` | Load a previously saved conversation |
| `exit` | Quit the chatbot |

## What I Learned
- REST API integration with requests library
- Environment variables for API key security
- JSON for saving and loading data
- Multi-turn conversation with message history
- Virtual environments and dependency management

## Tech Stack
- Python 3
- Groq API (llama-3.1-8b-instant)
- python-dotenv
