# Generate a random number between 1 and 9 (including 1 and 9).\n",
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. \n"

from random import * 

n = randint(1, 9)

print(n)

count = 1

user = int(input(" guess a number between 1 & 9 included : "))



while user != n :
    if user < n :
        print (" That's too low ")
        user = int(input(" try again : "))
    else :
        print (" That's too high ")
        user = int(input(" try again : "))
    count += 1 

print (" That's right baby!! ")
print ( "it took you just " + str(count) + " tries." )
