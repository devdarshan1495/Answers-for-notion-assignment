file_path = input("Enter the file path to read: ")
try:
    with open(file_path, 'r') as file:  
        contents = file.read()         
        print("File Contents:\n", contents)  
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
