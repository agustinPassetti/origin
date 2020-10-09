
our_password="pass123."
your_answer=""
number_of_try=0
number_of_max_try=8
max_try="not reached"

while your_answer != our_password and max_try != "reached": 
    if number_of_try < number_of_max_try:
        your_answer = input (" what is the password? ")
        number_of_try = number_of_try + 1
    else:
        max_try = "reached"


if max_try == "reached":
        print ("account blocked")
else:
        print("access granted")


