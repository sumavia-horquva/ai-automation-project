

import os
import ollama
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

client = ollama.Client(host=BASE_URL)

def ask_ai(question):
    response = client.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response["message"]["content"]

if __name__ == "__main__":
    print("AI Automation Backend Started!")

    question = input("Enter your question: ")
    answer = ask_ai(question)

    print("\nAI Response:")
    print(answer)
