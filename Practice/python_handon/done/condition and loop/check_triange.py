# Write a Python program to check a triangle is valid or not"

#ejemplo triangulo con dos lados iguales y uno distinto


def triangle_check (l1, l2, l3):

    if (l1 > l2 + l3) or (l2 > l1 + l3) or (l3 > l1 + l2) :
        print (" No, the lenghts wont work. ")
    elif (l1==l2+l3) or (l2==l1+l3) or (l3==l1+l2):
        print (" Yes! thats what im talking about! ")
    else:
        print (" Yes, a triangle can be formed out of it ")

l1 = int(input("lado 1: "))
l2 = int(input("lado 2: "))
l3 = int(input("lado 3: "))

triangle_check(l1, l2, l3)

