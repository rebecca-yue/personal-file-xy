import csv

input_path = "habitica_project/00_evidence/data/habitica_dailies_evidence.csv"

required_columns = [
    "task_name",
    "task_type",
    "due_frequency",
    "completion_status",
    "missed",
    "hp_effect",
    "context_recorded",
    "notes",
]

with open(input_path, "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames

    print("CSV headers:")
    print(headers)

    missing_columns = [col for col in required_columns if col not in headers]

    if missing_columns:
        print("Missing columns:")
        for col in missing_columns:
            print("-", col)
    else:
        print("All required columns are present.")

    row_count = 0
    daily_count = 0
    missed_count = 0

    for row in reader:
        row_count += 1
        if row["task_type"] == "Daily":
            daily_count += 1
        if row["missed"] == "yes":
            missed_count += 1

    print(f"Total rows: {row_count}")
    print(f"Daily rows: {daily_count}")
    print(f"Missed rows: {missed_count}")