
# ---------------------------------------------------------------\n",
# python best courses https://courses.tanpham.org/\n",
# ---------------------------------------------------------------\n",
# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. \n",
# The element value in the i-th row and j-th column of the array should be i*j.\n",


a = int(input(" number of rows : "))
b = int(input(" number of columns : "))

matrix = [[0 for i in range (b)]for j in range (a)]

for i in range(a):
    for j in range(b):
        matrix[i][j]= i*j

print (matrix)