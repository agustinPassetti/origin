#  Write a Python program to count the occurrences of each word in a given sentence"

def count_words (sentence) :
    count = 0
    for a in sentence:
        if a == ' ' :
            count += 1
    return (count + 1)


charla = input (" escriba nomas : ")

print(count_words(charla))


# otra opcion : (ésta está bien, yo no habia entendido)

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( word_count('the quick brown dog jumps over the lazy brown brown dog'))