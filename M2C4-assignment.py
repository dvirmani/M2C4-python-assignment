from decimal import Decimal
import math
# Exercise 1

# List
my_list = [5, 8, 10, 7, 9]


# Tuple
my_tuple = (5, 8, 10, 7, 9)

# float
my_float = 5.89

# integer
my_int = 5

# decimal
my_decimal = Decimal(5.89)

# Dictionary
my_dictionary = {
    'a': 'alpha',
    'b': 'beta',
    'g': 'gamma',
    'd': 'delta',
    'e': 'epsilon',
}

# Exercise 2

round_float = math.ceil(my_float)
print(round_float)

# Exercise 3
root = math.sqrt(my_float)

# Exercise 4

# first_element = my_dictionary['a']
first_element = my_dictionary.get('a', 'Element not found')

# Exercise 5

tuple_element = my_tuple[1]

# Exercise 6

my_list.append(12)

# Exercise 7

my_list[0] = 2

# Exercise 8

my_other_list = ['Apple', 'Tree', 'Ball', 'Drums', 'Zebra', 'Cup']
my_other_list.sort()

# Exercise 9
my_tuple += (12,)

