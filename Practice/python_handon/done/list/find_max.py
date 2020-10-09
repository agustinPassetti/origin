# Write a Python program to get the smallest number from a list.

l = [1, 2, -8, 0, 16, 1500000, 999999999, -8888888888888, 45]
#print (str(l))

def max_num_in_list (list):
    max = list[0]
    for element in list :
        if element > max :
            max = element
    return max
print (max_num_in_list(l))





