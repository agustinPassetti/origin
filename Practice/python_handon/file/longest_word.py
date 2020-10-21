# Write a python program to find the longest words in a file
# Using test.txt file in same folder


def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longest_word("/home/agustin/Documentos/vs_workspace/Practice/python_handon/file/test.txt"))