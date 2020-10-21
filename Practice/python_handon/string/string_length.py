# Write a Python program to calculate the length of a string.

def calculate_lenght(palabra):
    
    return len(palabra)
    

print(calculate_lenght("hola"))

# otra forma: 

def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('hello world'))