import os
import json
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

DATA_FILE = "student_data.json"


# ---------------------------------------------------------
# TOOL 1: Get student profile
# ---------------------------------------------------------

def get_student_profile():

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return json.dumps(data["student"])


# ---------------------------------------------------------
# TOOL 2: Get assignments
# ---------------------------------------------------------

def get_assignments():

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return json.dumps(data["assignments"])


# ---------------------------------------------------------
# Tool definitions given to the LLM
# ---------------------------------------------------------

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_student_profile",
            "description": "Get the student's private academic profile.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_assignments",
            "description": (
                "Get the student's private assignment data "
                "including subject, task, deadline, status and priority."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]


# ---------------------------------------------------------
# Tool execution
# ---------------------------------------------------------

def execute_tool(tool_name):

    if tool_name == "get_student_profile":
        return get_student_profile()

    elif tool_name == "get_assignments":
        return get_assignments()

    else:
        return "Unknown tool."


# ---------------------------------------------------------
# Agent
# ---------------------------------------------------------

def run_agent(user_request):

    messages = [
        {
            "role": "system",
            "content": """
You are an AI student assistant.

You have access to private student data through tools.

When the user's request requires private student information,
use the appropriate tool.

You should:
1. Understand the user's request.
2. Decide whether private data is required.
3. Select an appropriate tool.
4. Observe the tool result.
5. Continue reasoning if more information is required.
6. Provide a clear final answer.

Do not invent private student information.
"""
        },
        {
            "role": "user",
            "content": user_request
        }
    ]

    # -----------------------------------------------------
    # Agent loop
    # -----------------------------------------------------

    while True:

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            tools=tools,
            tool_choice="auto",
            temperature=0
        )

        message = response.choices[0].message

        # -------------------------------------------------
        # No tool required -> final response
        # -------------------------------------------------

        if not message.tool_calls:

            return message.content

        # -------------------------------------------------
        # Add assistant message
        # -------------------------------------------------

        messages.append(message)

        # -------------------------------------------------
        # Execute every requested tool
        # -------------------------------------------------

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name

            print(f"\n[Agent selected tool: {tool_name}]")

            result = execute_tool(tool_name)

            print("[Tool returned private data]")

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            )


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("AI AGENT")
    print("=" * 60)

    print("\nThe agent can access private student data through tools.")

    user_request = input("\nEnter your request: ")

    print("\nAgent working...")

    answer = run_agent(user_request)

    print("\nFinal Agent Response:")
    print(answer)