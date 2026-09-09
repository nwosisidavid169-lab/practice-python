# This file demonstrates different Python file modes:
# 'r'  - Read a file
# 'r+' - Read and write to a file
# 'a+' - Read and append to a file


# =================================
# OPENING AND READING A FILE ('r')
# =================================

# Store the file name/path in a variable
filename = 'beginner.txt'

# Open the file in read mode
with open(filename, 'r') as file:

    # Read everything inside the file
    content = file.read()

    # Print the content
    print(content)


# =================================
# WRITING AND READING A FILE ('r+')
# =================================

# Store the file name/path in a variable
filename = 'beginner.txt'

# Open the file for reading and writing
with open(filename, 'r+') as file:

    # Read everything inside the file
    content1 = file.read()

    # Print the original content
    print(content1)

    # Write new text at the current cursor position
    # After read(), the cursor is at the end
    file.write("\nI'm just a beginner for now")

    # Move the cursor back to the beginning
    # so we can read the updated file
    file.seek(0)

    # Read the updated content
    content2 = file.read()

    # Print the updated content
    print(content2)


# =================================
# APPENDING AND READING A FILE ('a+')
# =================================

# Store the file name/path in a variable
filename = 'beginner.txt'

# Open the file for appending and reading
with open(filename, 'a+') as file:

    # 'a+' starts at the end, so move to the beginning to read
    file.seek(0)

    # Read everything currently inside the file
    content1 = file.read()

    # Print the original content
    print(content1)

    # Append new text to the end of the file
    file.write("\nThe ending side")

    # Move back to the beginning
    # so we can read the updated content
    file.seek(0)

    # Read the updated content
    content2 = file.read()

    # Print the updated content
    print(content2)