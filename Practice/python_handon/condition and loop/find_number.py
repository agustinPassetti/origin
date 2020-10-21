#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700\n

guardo_array = []
for i in range(1500, 2700, 1) :
    if ((i % 7) == 0) and ((i % 5) == 0):
            print (str(i))
            guardo_array.append(str(i))

print(guardo_array)
print (',' .join(guardo_array))
