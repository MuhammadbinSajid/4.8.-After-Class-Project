# Function to create the mirrored right triangle pattern
def mirrored_right_triangle(rows):
    for i in range(1, rows + 1):
        # Print spaces first for mirroring
        print(" " * (rows - i) + "*" * i)

# Ask the user for the number of rows
rows = int(input("Enter the number of rows for the mirrored right triangle: "))

# Call the function to print the pattern
mirrored_right_triangle(rows)
