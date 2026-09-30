import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from calculator_tool import calculate_fee

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")

if not api_key:
    print("ERROR: OPENAI_API_KEY was not found.")
    exit()

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

question = """
A student has a course fee of ₹15,000 and receives a 25% scholarship.
What is the final fee?
"""

# Define the calculator tool
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_fee",
            "description": (
                "Calculate the final course fee after applying "
                "a scholarship percentage."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "total_fee": {
                        "type": "number",
                        "description": "The original course fee."
                    },
                    "scholarship_percent": {
                        "type": "number",
                        "description": "Scholarship percentage."
                    }
                },
                "required": [
                    "total_fee",
                    "scholarship_percent"
                ]
            }
        }
    }
]

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant. "
            "Use the calculator tool when an exact calculation is needed."
        )
    },
    {
        "role": "user",
        "content": question
    }
]

print("=" * 60)
print("LLM WITH ONE TOOL")
print("=" * 60)

# First LLM call
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

message = response.choices[0].message

# Check whether the LLM requested the tool
if message.tool_calls:

    print("\nTool call detected!")

    messages.append(message)

    for tool_call in message.tool_calls:

        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print("\nTool name:", function_name)
        print("Tool arguments:", arguments)

        if function_name == "calculate_fee":

            result = calculate_fee(
                arguments["total_fee"],
                arguments["scholarship_percent"]
            )

        else:
            result = "Unknown tool."

        print("\nTool result:")
        print(result)

        # Send tool result back to LLM
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            }
        )

    # Second LLM call
    final_response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools=tools
    )

    final_answer = final_response.choices[0].message.content

    print("\nFinal LLM answer:")
    print(final_answer)

else:

    print("\nNo tool was called.")

    print("\nFinal LLM answer:")
    print(message.content)