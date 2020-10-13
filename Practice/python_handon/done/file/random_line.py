# Write a Python program to read a random line from a file.
# Using test.txt


import random

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
  
print(random_line("/home/agustin/Documentos/vs_workspace/Practice/python_handon/file/test.txt"))
