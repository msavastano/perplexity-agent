# Perplexity Sonar Chat Agent

This project is a simple, web-based chat agent that uses the Perplexity Sonar API to generate responses. It's built with Python, Flask, and the `openai` library.

## How it Works

The application is built on a client-server architecture using a Flask back end and a simple HTML/CSS/JavaScript front end.

### Back End (Flask)

The core logic resides in `app.py`. The Flask application handles two main routes:

*   **`/` (Home):** When a user first visits the site, this route renders the main chat page (`index.html`). A crucial step here is the clearing of the session history. This ensures that each visit starts a fresh conversation.
*   **`/chat` (API Endpoint):** This endpoint receives POST requests from the front end containing the user's message. It manages the conversation flow by:
    1.  Retrieving the user's message from the request body.
    2.  Accessing the conversation history, which is stored in a Flask server-side session.
    3.  Appending the new user message to the history.
    4.  Sending the entire conversation history to the Perplexity Sonar API via the `openai` client library.
    5.  Receiving the AI-generated response.
    6.  Appending the assistant's response to the history.
    7.  Updating the session with the new history.
    8.  Returning the assistant's reply to the front end as a JSON object.

### Front End (HTML/JS)

The front end is a single-page interface that:
1.  Captures user input from a text field.
2.  Uses JavaScript's `fetch` API to send the message to the `/chat` endpoint.
3.  Receives the JSON response from the server.
4.  Dynamically creates and appends new chat bubbles to the display area for both user messages and agent replies.

### Chat Session History

The application maintains conversation context by keeping track of the chat history. This is accomplished using **Flask's session management**:

*   **Server-Side Sessions:** Flask sessions are used to store the conversation history for each user. A session is a storage area on the server that is unique to each client. Flask uses a cryptographically signed cookie to associate a client with their session data, preventing tampering.
*   **Initialization:** The application is configured with a `secret_key`, which is essential for securely signing the session cookie.
*   **Storing Messages:** The conversation, a list of message objects, is stored in the `session` dictionary under the key `'messages'`.
*   **State Management:**
    *   When a new conversation begins at the `/` route, any existing `'messages'` data is cleared from the session.
    *   In the `/chat` endpoint, the history is retrieved from the session, updated with the new user message and assistant reply, and then saved back into the session. This ensures that the context is maintained across multiple message exchanges within the same visit.

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