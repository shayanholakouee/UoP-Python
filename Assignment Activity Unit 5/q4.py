# Given weekly borrowing statistics
borrowed_books = [23, 19, 31, 27, 22, 30, 25]

# Extract records from week 2 to week 5 using slicing
# Note: Index 1 is Week 2, Index 5 is Week 6 (exclusive)
week_2_to_5 = borrowed_books[1:5]

# Replace the number of books borrowed in week 1 with 20
borrowed_books[0] = 20

# Display the updated list and the sliced portion
print("Updated borrowed_books list:", borrowed_books)
print("Sliced portion (Week 2 to Week 5):", week_2_to_5)