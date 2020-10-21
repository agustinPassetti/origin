# Write a Python class to convert a roman numeral to an integer
# Sample input
# 'MMMCMLXXXVI'
# 'MMMM'
# 'C'
# Sample output
# 3986                                                                                                          
# 4000                                                                                                          
# 100

class py_solution:

    def roman_to_int (self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if int_val > 0 and rom_val[s[i]] > rom_val[s[i - 1]] :
                int_val += rom_val[s[i]] - 2 * rom_val [s[i-1]]
            else:
                int_val += rom_val[s[i]]
        return int_val    

print(py_solution().roman_to_int('XIV'))
print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('C'))


# No esta dando buen resultado ( la rama else parece no funcionar)
# anda bien ahora, la identacion de return debia ser igual a la del for