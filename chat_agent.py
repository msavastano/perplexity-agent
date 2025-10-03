import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize client (Perplexity API is OpenAI-compatible)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # Make sure you've set this
    base_url="https://api.perplexity.ai"
)

def chat_loop(model="sonar-pro"):
    print("🤖 Perplexity Sonar Chat Agent (type 'exit' or 'quit' to stop)")
    messages = []

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye! 👋")
                break

            # Append user message to conversation
            messages.append({"role": "user", "content": user_input})

            # Get response from Sonar
            response = client.chat.completions.create(
                model=model,
                messages=messages
            )
            reply = response.choices[0].message.content

            # Show reply
            print(f"\n🤖 Agent: {reply}")

            # Append assistant reply for memory
            messages.append({"role": "assistant", "content": reply})

        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break

if __name__ == "__main__":
    chat_loop()
