# Write a Python program to check whether an alphabet is a vowel or consonant

sentence = input(" write some alphabet : ")

vowel = 0
consonant = 0 

for e in sentence :
    if e == "a" or e == "e" or e == "i" or e == "o" or e == "u" :
        vowel += 1
        print ( e + " is vowel")
    else:
        consonant += 1
        print(e + " is consonant")

print( "total vowels: " + str(vowel))
print("total consonants: " + str(consonant))