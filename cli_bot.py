import openai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create client
client = openai.OpenAI(api_key=api_key)

print("GPT ChatBot is running. Type 'exit' to quit.\n")

# Initial context with system prompt
messages = [
    {
        "role": "system",
        "content": "You are a friendly and helpful support chatbot. Keep responses short, clear, and useful."
    }
]

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print("Bot:", reply)