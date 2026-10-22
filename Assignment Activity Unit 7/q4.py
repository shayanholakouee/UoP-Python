import re

# Read all feedback entries.
with open("feedback.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

total_feedback = len(lines)
great_count = 0

# Convert each entry to lowercase and check its words.
for line in lines:
    words = re.findall(r"\b\w+\b", line.lower())

    if "great" in words:
        great_count += 1

# Create the formatted summary.
summary = (
    "=== Workshop Feedback Summary ===\n"
    f"Total Feedback: {total_feedback}\n"
    f"Mentions of 'Great': {great_count}\n"
)

# Save the summary to a new text file.
with open("summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

# Display the same summary.
print(f"{summary}", end="")