def count_vowels(s):
    if not s:
        return 0
    vowels = 'aeiouAEIOU'
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])


input_str = input("Enter a string: ")
result = count_vowels(input_str)
print(f"The number of vowels in the string is {result}.")
