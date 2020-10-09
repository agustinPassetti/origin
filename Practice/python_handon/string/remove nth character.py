# Write a Python program to remove the nth index character from a nonempty string"

def remove_char (sentence, i):
    first_part = sentence[: i]
    second_part = sentence[i+1 :]
    return first_part + second_part

caso1 = (remove_char("hayque sacarelespacio", 6))



print(caso1)

