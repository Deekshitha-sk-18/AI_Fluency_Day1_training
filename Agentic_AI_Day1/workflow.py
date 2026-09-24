import json
from datetime import datetime


DATA_FILE = "student_data.json"


def load_student_data():
    """Load private student data from the local JSON file."""
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_pending_assignments(assignments):
    """Return only assignments that are not completed."""
    return [
        assignment
        for assignment in assignments
        if assignment["status"].lower() != "completed"
    ]


def calculate_priority(assignment):
    """
    Calculate a numeric priority using predefined rules.

    High priority   = 3
    Medium priority = 2
    Low priority    = 1
    """

    priority_score = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    return priority_score.get(assignment["priority"], 0)


def sort_assignments(assignments):
    """Sort assignments by priority and then deadline."""

    return sorted(
        assignments,
        key=lambda assignment: (
            -calculate_priority(assignment),
            datetime.strptime(
                assignment["deadline"],
                "%Y-%m-%d"
            )
        )
    )


def main():

    print("=" * 60)
    print("RULE-BASED WORKFLOW")
    print("=" * 60)

    data = load_student_data()

    student = data["student"]
    assignments = data["assignments"]

    print(f"\nStudent: {student['name']}")
    print(f"Department: {student['department']}")
    print(f"Year: {student['year']}")

    pending = get_pending_assignments(assignments)

    sorted_tasks = sort_assignments(pending)

    print("\nAssignments to complete first:\n")

    for number, assignment in enumerate(sorted_tasks, start=1):

        print(
            f"{number}. {assignment['task']}"
            f" | Subject: {assignment['subject']}"
            f" | Deadline: {assignment['deadline']}"
            f" | Priority: {assignment['priority']}"
        )

    print("\nReason:")
    print("The workflow follows predefined rules:")
    print("1. Remove completed assignments.")
    print("2. Give High priority the highest score.")
    print("3. Sort by priority.")
    print("4. Use deadline to break ties.")


if __name__ == "__main__":
    main()