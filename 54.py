file_path = input("Enter the file path to count lines: ")

try:
    with open(file_path, 'r') as file:  
        lines = file.readlines()        
    print(f"The file contains {len(lines)} lines.")
except FileNotFoundError:
    print("Error: File not found.")
