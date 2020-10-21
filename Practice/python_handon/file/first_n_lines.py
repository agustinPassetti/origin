# Write a Python program to read first n lines of a file
# Use test.txt file

"""test = open("/home/agustin/Documentos/vs_workspace/Practice/python_handon/file/test.txt")

print (test.read(500))  #char amount

test.close()"""

#other way

def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
                        
file_read_from_head("/home/agustin/Documentos/vs_workspace/Practice/python_handon/file/test.txt",2)



