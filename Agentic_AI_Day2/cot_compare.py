import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


question = """
A student has three assignments:

Assignment A:
- Due tomorrow
- Takes 2 hours
- Medium difficulty

Assignment B:
- Due in three days
- Takes 5 hours
- Hard difficulty

Assignment C:
- Due tomorrow
- Takes 1 hour
- Easy difficulty

Determine which assignment should be prioritized first.

Consider:
1. Deadline
2. Estimated work
3. Difficulty

Give the final answer and a short reasoning summary.
Do not provide hidden chain-of-thought.
"""

print("=" * 60)
print("CHAIN-OF-THOUGHT STYLE REASONING")
print("=" * 60)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": (
                "Solve the problem carefully step by step internally. "
                "Return only the final answer and a concise reasoning summary, "
                "not private chain-of-thought."
            )
        },
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