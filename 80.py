def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(f"The file contains {len(lines)} lines.")
    except FileNotFoundError:
        print("The file does not exist.")

filename = input("Enter the file name to count lines: ")
count_lines_in_file(filename)
