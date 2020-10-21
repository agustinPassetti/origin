passw = input(" Enter a password, from 6 to 16 char, at least 1 a, 1 A, 1 [$#@]: ")

digit = 0
alpha = 0
other = 0

if (passw.__len__() >= 16) :

    print( " Too long!! ")

elif (passw.__len__() <= 6) :

    print( " Too short!! ")

else :
    for element in passw :

       if element.isdigit() :
           digit = digit + 1
        
       elif element.isalpha():
            alpha = alpha + 1

       else:
           other = other + 1


    #print( " digit: " + str(digit))
    #print(" alpha: " + str(alpha))
    #print (" other: " + str(other))
    #print ("cant letras " + str(passw.__len__()))


    if digit == 0 :
        print (" you need to add some numbers man! ")

    if alpha == 0 :
        print (" you need to add some letters man! ")

    if other == 0 :
        print (" you need to add some other chars man! ")

    if digit > 0 and alpha > 0 and other > 0 :
        print(" You know it!! perfect passsss!! ")