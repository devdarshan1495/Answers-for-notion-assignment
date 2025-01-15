def write_file(filename):
    text = input("Enter the text you want to write to the file: ")
    with open(filename, 'w') as file:
        file.write(text)
    print(f"Text has been written to {filename}.")

filename = input("Enter the file name to write to: ")
write_file(filename)
