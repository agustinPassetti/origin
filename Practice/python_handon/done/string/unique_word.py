# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)\n",
# Sample Words : red, white, black, red, green, black\n",
# Expected Result : black, green, red, white, red"

items = ", red, white, black, red, green, black"
#items = input("Input comma separated sequence of words: ")

words = [word for word in items.split(",")]


print(",".join(sorted(list(set(words)))))


#def unique_sorted_words (sentence) :
#intento fallido mio
