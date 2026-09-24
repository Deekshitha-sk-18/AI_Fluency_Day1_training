import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")


def run_agent(question):

    print("=" * 60)
    print("REACT AGENT")
    print("=" * 60)

    print("\nUser Question:")
    print(question)

    print("\nThought:")
    print("I need the current date to reason about the assignment deadline.")

    print("\nAction:")
    print("get_current_date()")

    current_date = get_current_date()

    print("\nObservation:")
    print(f"Current date = {current_date}")

    prompt = f"""
You are an assignment planning assistant.

User question:
{question}

Tool observation:
Today's date is {current_date}.

Use the tool observation and the information in the question
to provide a concise final answer.

Give only the final answer and a short explanation.
Do not reveal private chain-of-thought.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    print("\nFinal Answer:")
    print(response.choices[0].message.content)


question = """
I have an assignment due tomorrow and another assignment due
in three days. I want to prioritize the work that has the
closest deadline. Based on today's date, explain which deadline
comes first and what I should work on first.
"""

run_agent(question)