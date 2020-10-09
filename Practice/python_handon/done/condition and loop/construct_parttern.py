#  Write a Python program to construct the following pattern, using a nested for loop.\n",
"""# * \n",
    "# * * \n",
    "# * * * \n",
    "# * * * * \n",
    "# * * * * * \n",
    "# * * * * \n",
    "# * * * \n",
    "# * * \n",
    "# *"""

a = " *"
for i in range (1, 6):
    print(a * i)
for j in range (6, 0, -1):
    print(a * j)