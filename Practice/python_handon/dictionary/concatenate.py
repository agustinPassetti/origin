    # Write a Python script to concatenate following dictionaries to create a new one
    # Input
d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50, 6:60}
    # Output
    # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

d4 = {}

#d4 = dict(d1.items() + d2.items() + d3.items())

#print(d4)

# otra forma :

dic4 = {}
for d in (d1, d2, d3): 
    dic4.update(d)
print(dic4)