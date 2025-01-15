def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")

filename = input("Enter the file name to read: ")
read_file(filename)
