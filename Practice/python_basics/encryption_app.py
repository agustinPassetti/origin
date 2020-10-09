
def crypted (sentence) :
    translation = ""
    for element in sentence :
        if element in "Aa":
            translation = translation + "1"
        elif element in "Bb":
            translation = translation + "2"
        elif element in "Cc":
            translation = translation + "3"
        elif element in "Dd":
            translation = translation + "4"
        elif element in "Ee":
            translation = translation + "5"




        elif element in "Zz":
            translation = translation + ","
        

        else:
            translation = translation + element
    
    return translation

print(crypted(input(" write for crypt it : ")))