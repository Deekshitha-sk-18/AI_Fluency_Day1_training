import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("=" * 60)
print("PLAIN CHATBOT")
print("=" * 60)

print("\nThis chatbot does NOT access the student's private JSON file.")
print("It answers only using the information provided in the conversation.\n")

user_request = input("Enter your request: ")

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful student assistant. "
                "Answer the user's question clearly. "
                "You do not have access to any private files, databases, "
                "or external tools."
            )
        },
        {
            "role": "user",
            "content": user_request
        }
    ],
    temperature=0
)

print("\nChatbot response:")
print(response.choices[0].message.content)