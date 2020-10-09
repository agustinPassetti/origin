# Count the number of even and odd numbers from a series of numbers\n",
"""# Input \n",
    "# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple\n",
    "# Output\n",
    "# Number of even numbers : 4                                                                                    \n",
    "# Number of odd numbers : 5 """

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0

for x in numbers:
    if  ((x % 2)==0)  :
        even += 1
    else:
        odd += 1

print (" even = " + str(even))
print( " odd = " + str(odd))
