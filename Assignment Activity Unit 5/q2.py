# Create a tuple representing a borrower's details
borrower_details = ("John Doe", "B1023", "2025-10-15")

# Attempt to modify one element (will raise an error)
try:
    borrower_details[1] = "B9999"
except TypeError as error:
    print("Observation upon modification attempt:", error)

# Print the length of the tuple
print("Number of data fields:", len(borrower_details))

# Display each element using a loop
print("Borrower Information:")
for detail in borrower_details:
    print(detail)