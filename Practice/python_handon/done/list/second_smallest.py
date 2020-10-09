# Write a Python program to find the second smallest number in a list.
# input
# second_smallest([1, 2, -8, -2, 0])
# output
# -2

lista = [1, 2, -8, -2, 0]

def second_smallest (numbers):
    a1 = 999999
    a2 = float('inf') # no estoy seguro que significa pero creo que los inicializa sin valor??
    
    for element in numbers :

        if element <= a1:
            a1, a2 = element, a1
        elif element < a2:
            a2 = element
    return a2

print(second_smallest(lista))



    