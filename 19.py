numbers = []
while len(numbers) < 5:
        number = int(input(f"Enter number {len(numbers)+1}: "))
        numbers.append(number)
print("List:", numbers)
print("Length of list:", len(numbers))