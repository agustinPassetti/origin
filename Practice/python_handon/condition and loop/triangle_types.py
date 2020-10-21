# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

l1 = int(input("lado1?"))
l2 = int(input("lado2?"))
l3 = int(input("lado3?"))

if l1 == l2 == l3 :
    print("equilatero")

elif l1 == l2 != l3 or l1 != l2 == l3 or l1 == l3 != l2 :
    print ("isosceles")

else:
    print ("escaleno")