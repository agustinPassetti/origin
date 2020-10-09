# 'The quick brown fox jumps over the lazy dog.'\n",
# input : \"The quick brown fox jumps over the lazy dog.\"\n",
# output : \"dog. lazy the over jumps fox brown quick The" 


def revert_word (sentence) :
    for i in sentence.split('\n'):
        return(' '.join(i.split()[::-1]))
    
print(revert_word("The quick brown fox jumps over the lazy dog."))
print(revert_word("Python Exercises."))

