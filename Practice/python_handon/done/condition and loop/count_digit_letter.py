# Write a Python program that accepts a string and calculate the number of digits and letters\n",
"""# Sample Data : \"Python 3.2\"\n",
    "# Expected Output :\n",
    "# Letters 6 \n",
    "# Digits 2"""

sentence = input(" write anything whit number and letters: ")

letters = 0
digits = 0
others = 0

for element in sentence :
    if element.isalpha():
        letters = letters + 1
    elif element.isdigit():
        digits = digits + 1
    else:
        others = others + 1

print(letters)
print(digits)
print(others)

