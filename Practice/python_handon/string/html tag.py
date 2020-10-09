# Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result : 
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>



def add_html_tags (tag, sentence) :
    return "<%s>%s</%s>" % (tag, sentence, tag)




print(add_html_tags('ok', 'some title'))

