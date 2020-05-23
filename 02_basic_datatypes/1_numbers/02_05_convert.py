'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

# 1 Convert an int to a float
whole_number = 3
floating_number = float(whole_number)
print(floating_number)

# 2 Convert a float to an int

floating_number2 = 4.5
print(int(floating_number2))

# 3 Perform floor division using a float and an int

import math
f = math.floor(5.5)
print(f)
v = math.floor(6)
print(v)

# 4 Use two user inputted values to perform multiplication

number1 = float(input("Please select one number"))
number2 = float(input("Please select another number"))
product = (number1 * number2)
print(product)