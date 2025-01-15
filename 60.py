import json


file_path = "data.json"
try:
    with open(file_path, 'r') as file:
        data = json.load(file)  
    print("Original JSON data:")
    print(data)


    key_to_modify = input("Enter the key to modify: ")
    if key_to_modify in data:
        new_value = input(f"Enter the new value for '{key_to_modify}': ")
        data[key_to_modify] = new_value
    else:
        print(f"Key '{key_to_modify}' not found in the JSON file.")


    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4) 

    print("Updated JSON data written to the file.")

except FileNotFoundError:
    print("Error: JSON file not found.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON. Please ensure the file is properly formatted.")
