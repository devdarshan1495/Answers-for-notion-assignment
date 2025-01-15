import csv

file_path = input("Enter the path to the CSV file: ")

try:
    with open(file_path, 'r') as file:  
        reader = csv.reader(file)
        for row in reader:  
            print(row) 
except FileNotFoundError:
    print("Error: CSV file not found.")
