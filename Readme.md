# CLI Chatbot 🤖

A command-line chatbot built in Python using the Groq API.

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
   pip install requests python-dotenv
4. Create a .env file and add your Groq API key:
   GROQ_API_KEY=your-key-here
5. Run:
   python chatbot.py

## Commands
- Type any message to chat
- Type `exit` to quit
- Type `show history` to view conversation history
- Type `clear history` to clear conversation history
- Type `save conversation` to save the conversation
- Type `load conversation` to load a saved conversation


## Status
In progress