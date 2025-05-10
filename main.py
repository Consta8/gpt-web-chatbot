from flask import Flask, request, render_template, redirect
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

# Initial system message
system_prompt = {
    "role": "system",
    "content": "You are a friendly and helpful support chatbot. Keep responses short, clear, and useful."
}
chat_history = [system_prompt]

@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history

    if request.method == "POST":
        user_message = request.form.get("message")

        if user_message.strip().lower() == "/clear":
            chat_history = [system_prompt]
            return redirect("/")

        chat_history.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )

        bot_reply = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": bot_reply})

        return render_template("index.html", chat=chat_history[1:])  # exclude system message

    return render_template("index.html", chat=chat_history[1:])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)