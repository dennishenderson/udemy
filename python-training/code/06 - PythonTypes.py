"""
# Dictionaries
people = {'John': 32, "Rob": 23}
print(people["John"])
print(people)
"""

"""
# Dictionary Functions
numbers = {

    1: "one",
    2: "two",
    3: "three"
}

#print(1 in numbers)
print(numbers.get(5, "Key not found"))
"""

"""
# Tuples Can't overwrite
fruits = "Apple", "Mango", "Peach"
fruits[0] = "Orange" # returns an error
print(fruits[0])
"""

"""
# List Slicing
numbers = [0, 100, 200, 300, 400, 500, 600]

print(numbers[2:5])
print(numbers[:3])
print(numbers[3:])
print(numbers[1:6])
print(numbers[1:6:2])
print(numbers[1:6:3])
"""

"""
# List Comprehension
list = [x**2 for x in range(10) if x**2 % 2 == 0]
print(list)
"""

"""
# String Formatting
numbers = [12, 12, 2020]
newstring = "Date:{0}/{1}/{2}".format(numbers[0], numbers[1], numbers[2])
print(newstring)

a = "{x}/{y}".format(x=100, y=200)
print(a)
"""

"""
# String Functions
print(", ".join(["Apple", "Banana", "Mango"]))
print("Hello There!".replace("There", "World"))
newstring = "Hello There"
print(newstring.replace("There", "World"))
newstring2 = "This is a string"
print(newstring2.startswith("This"))
print(newstring2.endswith("string"))
print(newstring2.upper())
print(newstring2.lower())
"""

"""
# Numeric Functions
print(min(1, 2, 3, 4, 5))
print(max(1, 2, 3, 4, 5))
print(abs(-203))
"""

"""
# Coding Challenge 7 (My Solution)
products = {
    "book": 24.99,
    "music": 0.99,
    "egg": 4.79,
    "cookie": 3.98,
    "ps4": 249.99
}

print(products)
product = input("Enter product name: ")
if product in products:
    print("The cost of your {key} is ${value}.".format(key=product, value=products[product]))
else:
    print("Sorry '{key}' does not exist in the database.".format(key=product))

# Coding CHallenge 7 (Provided Solution)
products = {"Chair":40, "Sofa": 500, "Table": 90, "Monitor": 100 , "Carpet": 200}
newproduct = input('Enter product name')
if(newproduct in products):
    print(products.get(newproduct))
else:
    print('Product Not Found')
"""


# Coding Challenge 8 (My Solution)
# all odd numbers from 1 to 100
oddnumbers = [x for x in range(1, 101) if x % 2 == 1]
print(oddnumbers)

# Coding Challenge 8 (Given Solution)
new_list = list(range(1, 100))

for x in new_list:

    if x % 2 != 0:
        print(x)