# Agentic AI: From Prompt to Action

## 1. Scenario

### Course Fee Calculation After Scholarship

The scenario chosen for this task is calculating a student's final course fee after applying a scholarship.

For example:

* Original course fee: ₹15,000
* Scholarship: 25%
* Final fee: ₹11,250

This scenario demonstrates the difference between a plain Large Language Model (LLM) and an LLM connected to an external calculation tool.

The external tool used in this project is a Python calculator function called `calculate_fee()`.

---

## 2. What is a Large Language Model?

A Large Language Model (LLM) is an artificial intelligence model trained on large amounts of text data.

It can:

* Understand natural-language questions
* Generate text responses
* Explain concepts
* Summarize information
* Perform many reasoning and calculation tasks

In this project, the LLM receives the student's question and produces an answer.

The plain LLM version does not use any external tool.

---

## 3. What is an Agent?

An AI agent is a system that uses an LLM to decide what action should be taken to solve a user's request.

An agent can:

1. Understand the user's request.
2. Decide whether an external tool is useful.
3. Call the appropriate tool.
4. Receive the tool result.
5. Use the result to produce a final response.

In this project, the agent decides that the `calculate_fee` tool should be used for the scholarship calculation.

---

## 4. What is a Tool?

A tool is an external function or capability that an LLM can use to perform a specific task.

In this project, the tool is:

```text
calculate_fee()
```

The Python function receives:

* `total_fee`
* `scholarship_percent`

It calculates:

```text
Scholarship amount = Total fee × Scholarship percentage / 100

Final fee = Total fee − Scholarship amount
```

For example:

```text
Total fee = ₹15,000
Scholarship = 25%

Scholarship amount = 15,000 × 25 / 100
                   = ₹3,750

Final fee = 15,000 − 3,750
          = ₹11,250
```

---

## 5. What is a Tool Call?

A tool call happens when the LLM requests an external function to perform a task.

For the selected scenario, the LLM generated a tool call similar to:

```text
Tool name: calculate_fee

Arguments:
total_fee = 15000
scholarship_percent = 25
```

The Python program then executes the function and returns:

```text
Original fee: ₹15000.00
Scholarship: 25%
Scholarship amount: ₹3750.00
Final fee: ₹11250.00
```

The result is then sent back to the LLM.

---

## 6. What is a Tool Schema?

A tool schema describes the tool to the LLM.

It tells the LLM:

* The tool name
* What the tool does
* Which parameters are required
* The data type of each parameter

The schema used in this project contains:

```text
Tool name:
calculate_fee

Parameters:
total_fee → number
scholarship_percent → number
```

The schema helps the LLM understand when and how to use the tool.

---

## 7. Step-by-Step Tool Call Flow

The workflow of this project is:

```text
User Question
      ↓
      LLM
      ↓
Decides calculation is needed
      ↓
Tool Call
      ↓
calculate_fee()
      ↓
Python calculation
      ↓
Tool Result
      ↓
LLM receives result
      ↓
Final Answer
```

For the example:

```text
User:
₹15,000 fee + 25% scholarship
          ↓
LLM
          ↓
calculate_fee(15000, 25)
          ↓
Python Tool
          ↓
₹11,250
          ↓
LLM
          ↓
Final Answer: ₹11,250
```

---

## 8. Why Should the Tool Return Text Even When Something Goes Wrong?

A tool should return a clear text result instead of abruptly stopping the entire program.

For example, if the tool receives invalid input, it can return:

```text
Error: total_fee must be a positive number.
```

This allows the LLM to understand the problem and provide a useful response to the user.

Returning text also keeps communication between the tool and the LLM simple and predictable.

---

## 9. Plain LLM vs LLM With Tool

| Feature                                   | Plain LLM | LLM + Tool                  |
| ----------------------------------------- | --------- | --------------------------- |
| Uses LLM                                  | Yes       | Yes                         |
| External tool                             | No        | Yes                         |
| Python calculator                         | No        | Yes                         |
| Can answer general questions              | Yes       | Yes                         |
| Can perform calculation                   | Often yes | Yes, using the defined tool |
| Tool call visible                         | No        | Yes                         |
| Calculation is delegated to external code | No        | Yes                         |
| Result can be inspected                   | Limited   | Yes                         |
| Suitable for simple explanations          | Yes       | Yes                         |
| Suitable for tool-backed calculations     | No        | Yes                         |

The important difference is not that a plain LLM is incapable of arithmetic. A modern LLM can often calculate simple values.

The difference is that the tool-enabled system explicitly delegates the calculation to an external Python function. This makes the calculation operation inspectable and reproducible.

---

## 10. Implementation

The project contains three main Python files.

### `calculator_tool.py`

Contains the external calculation function:

```python
calculate_fee(total_fee, scholarship_percent)
```

### `no_tool.py`

Sends the question directly to the LLM without providing a tool.

### `with_tool.py`

Provides the `calculate_fee` tool to the LLM.

The LLM can request the tool, the Python function performs the calculation, and the result is returned to the LLM.

---

## 11. Observations

### Question 1

**Question:**

A student has a course fee of ₹15,000 and receives a 25% scholarship. What is the final fee?

### Plain LLM

The plain LLM calculated:

```text
₹15,000 − 25% of ₹15,000
= ₹15,000 − ₹3,750
= ₹11,250
```

### LLM With Tool

The tool-enabled version generated:

```text
Tool name: calculate_fee

Arguments:
total_fee = 15000
scholarship_percent = 25
```

The tool returned:

```text
Final fee: ₹11250.00
```

The LLM then generated the final answer:

```text
Final fee: ₹11,250.00
```

---

### Question 2

**Question:**

What is a scholarship?

This type of question can be answered directly by the LLM because it mainly requires an explanation rather than an external calculation.

The tool is not necessary for this question.

---

### Question 3

**Question:**

A course costs ₹20,000 and a student receives a 10% scholarship. What is the final fee?

The calculation is:

```text
Scholarship amount
= ₹20,000 × 10 / 100
= ₹2,000

Final fee
= ₹20,000 − ₹2,000
= ₹18,000
```

This question is suitable for the calculator tool because the calculation can be explicitly delegated to the external Python function.

---

## 12. When is a Plain LLM Enough?

A plain LLM is generally sufficient when the task involves:

* Definitions
* General explanations
* Summarization
* Rewriting
* Brainstorming
* Simple conceptual questions

For example:

```text
What is a scholarship?
```

does not require the calculator tool.

---

## 13. When is a Tool Useful?

A tool becomes useful when the task benefits from an external operation or source.

Examples include:

* Exact calculations
* File reading
* Database access
* Live information lookup
* External APIs
* Data processing

In this project, the calculator tool provides an explicit and reproducible calculation operation.

---

## 14. Project File Structure

The final project structure is:

```text
Agentic_AI_day 3/
│
├── calculator_tool.py
├── no_tool.py
├── with_tool.py
├── analysis.md
├── requirements.txt
├── .gitignore
│
└── screenshots/
    ├── no_tool_output.png
    └── tool_output.png
```

The `.env` file is also used locally for the API credentials, but it should NOT be uploaded to GitHub.

The `.venv` folder should also NOT be uploaded.

---

## 15. Conclusion

This project demonstrates the transition from a plain LLM to an LLM-based system that can use an external tool.

The plain LLM can answer the scholarship question directly.

The tool-enabled version follows a different workflow:

```text
User
 ↓
LLM
 ↓
Tool Call
 ↓
Python Calculator
 ↓
Tool Result
 ↓
LLM
 ↓
Final Answer
```

The experiment shows that tools extend the capabilities of an LLM by allowing it to interact with external functions and data.

The main learning from this task is that an LLM does not have to perform every operation itself. An agent can decide when an external tool is appropriate, call the tool using a defined schema, receive the result, and use that result to generate the final response.
