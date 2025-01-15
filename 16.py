number = int(input("Enter number: "))
power = int(input("Enter exponent: "))
result = 1
for i in range(number):
    result *= number
print("Result:", result)