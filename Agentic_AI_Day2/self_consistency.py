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

A: Due tomorrow, takes 2 hours.
B: Due in three days, takes 5 hours.
C: Due tomorrow, takes 1 hour.

If the student wants to reduce the immediate deadline risk,
which assignment should receive priority?

Return only:
A
B
or C
"""

print("=" * 60)
print("SELF-CONSISTENCY TEST")
print("=" * 60)

answers = []

for i in range(5):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.7
    )

    answer = response.choices[0].message.content.strip()

    answers.append(answer)

    print(f"Run {i + 1}: {answer}")


print("\nAll responses:")
for i, answer in enumerate(answers, start=1):
    print(f"{i}. {answer}")

print("\nNow repeat the experiment with temperature=0.")