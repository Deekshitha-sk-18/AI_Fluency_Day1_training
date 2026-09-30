import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")

if not api_key:
    print("ERROR: OPENAI_API_KEY was not found.")
    exit()

# Create OpenAI-compatible client
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

# Question for the LLM
question = """
A student has a course fee of ₹15,000 and receives a 25% scholarship.
What is the final fee after the scholarship?
Explain the calculation.
"""

print("=" * 60)
print("PLAIN LLM - NO TOOL")
print("=" * 60)

# Ask the LLM directly
response = client.chat.completions.create(
   model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful assistant. "
                "Answer the user's question using only your own knowledge. "
                "Do not use external tools."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

answer = response.choices[0].message.content

print("\nQuestion:")
print(question)

print("LLM Answer:")
print(answer)