def append_to_file(filename):
    text = input("Enter the text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(text + '\n')
    print(f"Text has been appended to {filename}.")

filename = input("Enter the file name to append to: ")
append_to_file(filename)
