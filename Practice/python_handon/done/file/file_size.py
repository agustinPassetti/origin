# Write a Python program to get the file size of a plain file.
# # Use test.txt file at same folder.


import os
#os.stat('test.txt').st_size
a = os.path.getsize("/home/agustin/Documentos/vs_workspace/Practice/python_handon/file/test.txt")
print("the files has " + str(a) + " bytes.")



"""from pathlib import Path
b = Path('/home/agustin/Documentos/vs_workspace/Practice/python_handon/file/test.txt').stat()

print (b)"""