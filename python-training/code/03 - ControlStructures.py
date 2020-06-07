"""
# if/else
age = int(input('Enter your age: '))

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult')
"""

"""
# elif
grades = int(input('Enter your grades: '))

if grades >= 90:
    print('Grade A')
elif grades >= 80:
    print('Grade B')
elif grades >= 70:
    print('Grade C')
elif grades >= 60:
    print('Grade D')
else:
    print('Grade F')
"""

"""
# lists
names = ["Dennis", "Jennifer", "Elijah", "Zachariah"]
print(names[1])

numbers = [1, 2, 3, 4, 5]
print(numbers[4])

abc = []
print(abc)
"""

"""
# List Operations
numbers = [1, 1, 1, 1, 1]
newnumbers = [2, 2, 2, 2, 2]
fruits = ["Apple", "Mango", "Peach"]

# numbers[2] = 5
# print(numbers)
# print(numbers+newnumbers)
# print(numbers*3)
print(fruits)
print("Apple" in fruits)
fruits += ["Orange"]
print(fruits)
print("Orange" in fruits)
"""

"""
# List Functions
fruits = ["Apple", "Mango", "Peach", "Orange"]
fruits.append("Banana")
print(fruits)
print(len(fruits))
fruits.insert(1, "Strawberry")
print(fruits)
print(fruits.index("Peach"))
"""


# Range Function
# numbers = list(range(10))
# numbers = list(range(3, 8))
numbers = list(range(1, 30, 3))
print(numbers)


"""
# Functions
def function1():
    print("Dennis")
    print("Strawberry")
    print("Tampa")

function1()
function1()
"""

"""
# For Loop
for x in range(1,6):
    # print(x)
    print(str(x) + " - Dennis")

fruits = ["Apple", "Banana", "Peach", "Orange"]
for x in fruits:
    print(x)

for x in range(0,21,2):
    print(x)
"""

"""
# Boolean logic
username = "user"
password = "admin123"

if username == "admin" and password == "admin123":
    print("Valid User")
else:
    print("Invalid User")
"""

"""
# While Loop
counter = 0
while counter <= 10:
    print(counter)
    counter += 1
"""

"""
# Coding Challenge 2
food = ["Strawberry", "Pizza", "Candy", "Seafood", "In-N-Out"]
print(food[2])
food.append("Cake")
print(food)
food.insert(3, "Tacos")
print(food)
"""

"""
# Coding Challenge 3
for x in range(1, 6):
    print("I am a programmer")

def display_square():
    for x in range(1, 10):
        print(x ** x)

display_square()
"""