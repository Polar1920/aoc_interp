# Import the necessary modules
import os

# Define the path to the text file
file_path = os.path.join(os.path.dirname(__file__), "pantufla.txt")

# Open the text file in read mode
with open(file_path, "r") as f:
    # Read the contents of the file
    file_contents = f.read()

# Print the contents of the file
print(file_contents)
