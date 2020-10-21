# Write a Python program to remove duplicates from a list.



a = [10,20,30,20,10,50,60,40,80,50,40, 30, 40, 80, 100, 100, 100, 200, 80]
# Output {40, 10, 80, 50, 20, 60, 30} 

dup_items = set()

uniq_items = []

for element in a :
    if element not in dup_items:
        uniq_items.append(element)
        dup_items.add(element)
print("unicos : " + str(uniq_items))
print("duplicados : " + str(dup_items))

# las dos listas muestran los valores unicos de distintas formas.