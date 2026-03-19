import csv
import os

output_path = output_path = "habitica_project/00_evidence/data/habitica_dailies_evidence.csv"

rows = [
    {
        "task_name": "Drink water",
        "task_type": "Daily",
        "due_frequency": "Every day",
        "completion_status": "completed",
        "missed": "no",
        "hp_effect": "0",
        "context_recorded": "no",
        "notes": "Basic repeated self-care task",
    },
    {
        "task_name": "Take medication",
        "task_type": "Daily",
        "due_frequency": "Every day",
        "completion_status": "missed",
        "missed": "yes",
        "hp_effect": "-10",
        "context_recorded": "no",
        "notes": "Missed daily with no contextual explanation",
    },
    {
        "task_name": "Reply to messages",
        "task_type": "To-Do",
        "due_frequency": "One-off",
        "completion_status": "not completed",
        "missed": "no",
        "hp_effect": "0",
        "context_recorded": "no",
        "notes": "One-off task does not operate like a Daily",
    },
    {
        "task_name": "Stretch for 10 minutes",
        "task_type": "Daily",
        "due_frequency": "Every day",
        "completion_status": "completed",
        "missed": "no",
        "hp_effect": "0",
        "context_recorded": "no",
        "notes": "Routine task treated as repeatable behavioural object",
    },
    {
        "task_name": "Pay electricity bill",
        "task_type": "To-Do",
        "due_frequency": "One-off",
        "completion_status": "completed",
        "missed": "no",
        "hp_effect": "0",
        "context_recorded": "no",
        "notes": "Single deadline task",
    },
    {
        "task_name": "Log mood",
        "task_type": "Daily",
        "due_frequency": "Every day",
        "completion_status": "missed",
        "missed": "yes",
        "hp_effect": "-10",
        "context_recorded": "no",
        "notes": "No field for emotional difficulty or overload",
    },
    {
        "task_name": "Read 5 pages",
        "task_type": "Daily",
        "due_frequency": "Every day",
        "completion_status": "missed",
        "missed": "yes",
        "hp_effect": "-10",
        "context_recorded": "no",
        "notes": "Missed task becomes measurable loss",
    },
    {
        "task_name": "Buy groceries",
        "task_type": "To-Do",
        "due_frequency": "One-off",
        "completion_status": "completed",
        "missed": "no",
        "hp_effect": "0",
        "context_recorded": "no",
        "notes": "Single completion logic",
    },
    {
        "task_name": "Walk outside",
        "task_type": "Habit",
        "due_frequency": "Flexible",
        "completion_status": "completed",
        "missed": "no",
        "hp_effect": "0",
        "context_recorded": "no",
        "notes": "Habit differs from Daily in governance logic",
    },
    {
        "task_name": "Rest",
        "task_type": "Reward",
        "due_frequency": "Optional",
        "completion_status": "completed",
        "missed": "no",
        "hp_effect": "0",
        "context_recorded": "no",
        "notes": "Reward category works differently from required repetition",
    },
]

fieldnames = [
    "task_name",
    "task_type",
    "due_frequency",
    "completion_status",
    "missed",
    "hp_effect",
    "context_recorded",
    "notes",
]

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"CSV created at: {output_path}")
