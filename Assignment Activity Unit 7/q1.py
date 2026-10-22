raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "

# Remove outside spaces and convert to lowercase.
feedback = raw_feedback.strip().lower()

# Replace the wording and remove extra internal spaces.
feedback = feedback.replace("speaker", "presenter")
feedback = " ".join(feedback.split())

# Convert to title case and display using an f-string.
feedback = feedback.title()
print(f"Cleaned feedback: {feedback}")