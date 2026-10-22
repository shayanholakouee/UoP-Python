feedback_list = [
    "The Presenter Was Great But The Room Was Cold",
    "Helpful Slides And Clear Examples",
    "The Session Ended On Time"
]

# Write three messages, each on a separate line.
with open("feedback.txt", "w", encoding="utf-8") as file:
    for feedback in feedback_list:
        file.write(f"{feedback}\n")

# Read and display the original messages.
print("Original feedback:")
with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip("\n"))

# Append one additional message.
with open("feedback.txt", "a", encoding="utf-8") as file:
    file.write("Great Practical Workshop\n")

# Read and display the updated messages.
print("\nUpdated feedback:")
with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip("\n"))