source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

try:
    with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
        dest.write(src.read()) 
    print(f"Contents copied successfully from {source_file} to {destination_file}.")
except FileNotFoundError:
    print("Error: Source file not found.")
