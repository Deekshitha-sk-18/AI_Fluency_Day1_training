import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client =  OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


question = """
I have three student assignments:

Assignment A:
- Due tomorrow
- Estimated time: 2 hours
- Difficulty: medium

Assignment B:
- Due in three days
- Estimated time: 5 hours
- Difficulty: hard

Assignment C:
- Due tomorrow
- Estimated time: 1 hour
- Difficulty: easy

Which assignment should I prioritize first?
Explain your answer briefly.
"""

print("=" * 60)
print("DIRECT PROMPTING")
print("=" * 60)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0
)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(response.choices[0].message.content)