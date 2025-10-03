import os
from flask import Flask, render_template, request, jsonify, session
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# A secret key is needed to use sessions
app.secret_key = os.urandom(24)

# Initialize client (Perplexity API is OpenAI-compatible)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.perplexity.ai"
)

@app.route("/")
def home():
    # Clear session history on new visit
    session.pop('messages', None)
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Get conversation history from session, or initialize it
    messages = session.get('messages', [])
    messages.append({"role": "user", "content": user_input})

    try:
        # Get response from Sonar
        response = client.chat.completions.create(
            model="sonar-pro",
            messages=messages
        )
        reply = response.choices[0].message.content

        # Append assistant reply and update session
        messages.append({"role": "assistant", "content": reply})
        session['messages'] = messages

        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Error: {e}")
        # Don't save the errored conversation turn
        session['messages'] = messages[:-1] # Remove user's last message if API fails
        return jsonify({"error": "Sorry, something went wrong."}), 500

if __name__ == "__main__":
    app.run(debug=True)