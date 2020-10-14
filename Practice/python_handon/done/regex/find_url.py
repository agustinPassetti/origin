# Write a Python program to find urls in a string.\n",
# \n",
# Input\n",
# '<p>Contents :</p><a href=\"https://www.w3schools.com/html/\">Python Examples</a><a href=\"http://github.com\">Even More Examples</a>'\n",
# \n",
# Output\n",
# Urls:  ['https://w3resource.com', 'http://github.com']

import re

text = "<p>Contents :</p><a href=\"https://www.w3schools.com/html/\">Python Examples</a><a href=\"http://github.com\">Even More Examples</a>"

urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text)

print(urls)

