# Write a Python class to reverse a string word by word.
# Input "hello world"
# Output "world hello"

class Revert_word ():

    def __init__(self):
        self.str1 = ""
    def get_word(self):
        self.str1 = input("Give me a sentence please: ")

    def print_reverted(self):
        print (' '.join(reversed(self.str1.split())))

        #print(self.str1.upper())


str1 = Revert_word()
str1.get_word()
str1.print_reverted()

# Otra forma:

class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))
print(py_solution().reverse_words('hello world'))