
# My AI Chatbot 🤖

A beginner-friendly AI chatbot built with Python and Google's Gemini API.

## Features

- Answers questions using an AI model
- Supports follow-up questions in the same conversation
- Runs in the VS Code terminal
- Keeps the API key in a separate environment file

## Technologies Used

- Python
- Google Gen AI Python SDK
- Gemini API
- Visual Studio Code

## Requirements

- Python installed
- A Gemini API key with API access
- The required Python packages

## Setup

1. Clone or download this repository.
2. Install the dependencies:

   ```bash
   python -m pip install google-genai python-dotenv
   ```

3. Create a `.env` file in the project folder and add:

   ```text
   GEMINI_API_KEY=your_api_key_here
   ```

4. Run the chatbot:

   ```bash
   python chatbot.py
   ```

## Security

Never share your API key or upload your `.env` file to GitHub.

## About

Built as a learning project while exploring Python and AI development.
