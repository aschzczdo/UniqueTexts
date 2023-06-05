import os

# Function to read a file and return lines
def read_lines(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            lines.append(line.strip().lower())
    return lines

# Function to write lines to a file.
def write_lines(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))

# Folder path containing the .txt files
folder_path = r'<YOUR_TXT_FOLDER_PATH'
result_file = 'result.txt'

# Get the list of .txt files in the folder
txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

# List to store lines from all files
all_lines = []

# Iterate over each .txt file and get lines
for txt_file in txt_files:
    file_path = os.path.join(folder_path, txt_file)
    lines = read_lines(file_path)
    all_lines.extend(lines)

# Remove duplicate lines
unique_lines = set(all_lines)

# Write unique lines to the result.txt file
result_file_path = os.path.join(folder_path, result_file)
write_lines(result_file_path, unique_lines)

print("result.txt file created with unique lines.")
