# Write a Python function that takes a list of words and returns the length of the longest one"

words = ['ahoramaslargoagus', 'agustin', 'agustinlargo', 'cortina']

#print (len(words[0]))



def print_longest (lista) :

    a = len(lista[0])
    #b = lista [1]

    for element in lista :
        if len(element) > a :
            a = len(element)
    
    return a

print(print_longest(words))


# otra forma :

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0]
    #return word_len [:]
print(find_longest_word(["PHP", "Exercises", "Backend"]))



