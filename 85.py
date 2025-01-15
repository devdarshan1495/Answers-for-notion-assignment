# i haven't been taught this so chatGPT 
import csv

def read_csv(filename):
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print("The file does not exist.")


filename = input("Enter the CSV file name to read: ")
read_csv(filename)
