# Write a Python program to count the number of characters (character frequency) in a string.
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

import collections

sentence = input("write or die: ")

my_list = []

for letter in sentence :
    my_list.append(letter)


contador = collections.Counter(my_list)

print(contador)


#otra forma:


def char_frequency(palabra):
    dict = {}
    for letra in palabra:
        keys = dict.keys()
        if letra in keys:
            dict[letra] += 1
        else:
            dict[letra] = 1
    return dict
print(char_frequency('google q lo parió'))