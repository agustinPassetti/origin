#comentario somple linea

"""comen
tario
multi
linea"""

name1=input("name1:")
name2=input("name2:")
name3=input("name3:")

slices=input("how many slices in the pizza?")
price=input("what is the price of the pizza?")

percent_eatten_1=input(name1+" how much did you ate? % ")
percent_eatten_2=input(name2+" how much did you ate? % ")
percent_eatten_3=input(name3+" how much did you ate? % ")

number_of_slices_p1=(float(percent_eatten_1)/100)*float(slices)
number_of_slices_p2=(float(percent_eatten_2)/100)*float(slices)
number_of_slices_p3=(float(percent_eatten_3)/100)*float(slices)

price_paid_p1=(float(percent_eatten_1)/100)*float(price)
price_paid_p2=(float(percent_eatten_2)/100)*float(price)
price_paid_p3=(float(percent_eatten_3)/100)*float(price)

print(str(name1) + " ate " + str(number_of_slices_p1) + " and paid " + str(price_paid_p1) + " dolars ")
print(str(name2) + " ate " + str(number_of_slices_p2) + " and paid " + str(price_paid_p2) + " dolars ")
print(str(name3) + " ate " + str(number_of_slices_p3) + " and paid " + str(price_paid_p3) + " dolars ")
