    # Check if a given key already exists in a dictionary
    # input
    # d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    # is_key_present(5)
    # is_key_present(9)
    # output
    # Key is present in the dictionary                                                                              
    # Key is not present in the dictionary

"""d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):

  
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')

  #for i in d :
    #print(d[i])


is_key_present(5)
#is_key_present(10)"""

# testing if value is

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_value_present(x):
  
  for i in d:
      if x == d[i]:
        print('value is present in the dictionary')
      else:
        print('value is not present in the dictionary')
#is_value_present(d[5], 5)
is_value_present(60)


#print(d[5], 5)