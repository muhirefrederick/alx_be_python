# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop for columns in each row
    for col in range(size):
        print("*", end="")  # Print * without newline
    print()  # Print newline after each row
    row += 1
