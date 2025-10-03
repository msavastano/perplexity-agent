# Perplexity Sonar Chat Agent

This project is a simple, web-based chat agent that uses the Perplexity Sonar API to generate responses. It's built with Python, Flask, and the `openai` library.

## How it Works

The application uses a Flask back end to serve a simple HTML, CSS, and JavaScript front end. When a user sends a message:

1.  The front end sends the message to the `/chat` endpoint on the Flask server.
2.  The Flask server appends the message to the conversation history.
3.  It sends the entire conversation to the Perplexity Sonar API.
4.  The API returns a response, which the server sends back to the front end.
5.  The front end displays the agent's reply in the chat window.

## Features

*   **Web-Based Interface:** A clean and simple chat interface that runs in your browser.
*   **Interactive Chat:** Engage in a real-time conversation with the Perplexity Sonar model.
*   **Conversation Memory:** The agent remembers the context of the conversation for more coherent and relevant responses.
*   **Simple and Extensible:** The code is straightforward and can be easily modified or integrated into other applications.

## Getting Started

### Prerequisites

*   Python 3.x
*   An API key from Perplexity AI.

### Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API key:**
    Create a file named `.env` in the root of the project and add your API key:
    ```
    OPENAI_API_KEY="your_perplexity_api_key"
    ```
    The application uses `python-dotenv` to load this key as an environment variable.

5.  **Run the application:**
    ```bash
    flask run
    ```
    Or, for development mode:
    ```bash
    python app.py
    ```

6.  **Open your browser:**
    Navigate to `http://127.0.0.1:5000` to start chatting with the agent.