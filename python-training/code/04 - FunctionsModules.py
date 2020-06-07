"""
# Function Arguments
def add(a, b):
    print(a + b)


add(10, 20)
add(100, 200)
"""

"""
# Function Returning Values
def add(a, b):
    c = a + b
    return c


result = add(100, 200)
print(result)
"""

"""
# Passing functions as arguments
def add(a, b):
    return a + b


def square(c):
    return c * c


result = square(add(2, 3))
print(result)
"""

"""
# Modules
import random

for x in range(5):
    result = random.randint(1,6)
    print(result)
"""


# Coding Challenge 4
def calculate_BMI(new_weight, new_height):
    new_bmi = new_weight / (pow(new_height, 2))
    return new_bmi


weight = float(input('Enter weight in Kgs'))
height = float(input('Enter height in meters'))
bmi = calculate_BMI(weight, height)
print(bmi)