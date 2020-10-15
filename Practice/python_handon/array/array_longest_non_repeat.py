# Challenge\n",
# Given a string, find the length of the longest substring\n",
# without repeating characters.\n",
# Examples:\n",
# Given \"abcabcbb\", the answer is \"abc\", which the length is 3.\n",
# Given \"bbbbb\", the answer is \"b\", with the length of 1.\n",
# Given \"pwwkew\", the answer is \"wke\", with the length of 3.\n"

str1 = "abcdeaccbb"

def longest_sub_string(str1):

    max_length = 0

    for index, char in enumerate(str1) :

        i = index
        sub_string = []

        while (i < len(str1)) and (str1[i] not in sub_string) :
            sub_string.append(str1[i])
            i += 1 
        
        if max_length < len(sub_string):
            max_length = len (sub_string)

        #print (sub_string)  

    #print (max_length)

    return max_length


print(longest_sub_string(str1))
