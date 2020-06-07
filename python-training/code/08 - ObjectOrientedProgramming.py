"""
# Creating a Class
class Teddy:
    quantity = 200


teddy1 = Teddy()
teddy2 = Teddy()
print(teddy1.quantity)
print(teddy2.quantity)
"""

"""
# Instance Attributes
class Teddy:
    quantity = 200

    def __init__(self, name, color):
        self.name = name
        self.color = color


teddy1 = Teddy("Ted", "Red")
print(teddy1.name)
print(teddy1.color)

teddy2 = Teddy("Rob", "Brown")
print(teddy2.name)
print(teddy2.color)
"""

"""
# Implementing Methods
class Teddy:
    quantity = 200

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def change_color(self, color):
        print("This is the color method")
        self.color = color

    def change_name(self, name):
        print("This is the name method")
        self.name = name


teddy1 = Teddy("Ted", "Red")
print(teddy1.name)
print(teddy1.color)

teddy1.change_color("Orange")
print(teddy1.name)
print(teddy1.color)

teddy1.change_name("Dukey")
print(teddy1.name)
print(teddy1.color)
"""

"""
# Function based vs OOP
# Function
# def abc():
#     name = input("Enter name: ")
#     age = input("Enter age: ")
#     print(name)
#     print(age)
#
#
# abc()

# OOP
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self, name, age):
        self.name = name
        self.age = age

    def put_data(self):
        print(self.name)
        print(self.age)


student1 = Student("", "")
name = input("Enter name: ")
age = input("Enter age: ")
student1.get_data(name, age)
student1.put_data()
"""

"""
# Inheritance
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")

    def put_data(self):
        print(self.name)
        print(self.age)

class ScienceStudent(Student):

    def science(self):
        print("This is a science method")


a = ScienceStudent("", "")
a.get_data()
a.put_data()
"""

"""
# Multiple Inheritance
class A:
    def a_method(self):
        print("This is a method from A")

class B:
    def b_method(self):
        print("This is a method from B")

class C(A, B):
    def c_method(self):
        print("This is a method from C")

c_object = C()
c_object.a_method()
c_object.b_method()
c_object.c_method()
"""

"""
# Multi-Level Inheritance
class A:
    def a_method(self):
        print("This is a method from A")

class B(A):
    def b_method(self):
        print("This is a method from B")

class C(B):
    def c_method(self):
        print("This is a method from C")

c_object = C()
c_object.a_method()
c_object.b_method()
c_object.c_method()
"""

"""
# Recursion (function calling itself)
def factorial(x):
    if(x == 1):
        return 1
    else:
        return x * (factorial(x-1))

print(factorial(5))
"""

"""
# Sets
# numbers = {1, 2, 3, 4, 5, 6}
# print(5 in numbers)
# numbers.add(9)
# numbers.remove(4)
# print(numbers)

seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8}
print(seta | setb)
print(seta & setb)
print(seta - setb)
"""

"""
# Itertools
# Count to infinity
from itertools import count

for i in count(3):
    print(i)

    if i >= 20:
        break

# accumulate and takewhile
from itertools import accumulate, takewhile

numbers = list(accumulate(range(8)))
print(numbers)
print(list(takewhile(lambda x: x <= 10, numbers)))
"""

"""
# Operator Overloading
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    

point1 = Point(1, 4)
point2 = Point(2, 8)
print(point1 + point2)
"""

"""
# Encapsulation / Data Hiding
class Myclass:
    __hiddenvariable = 0


    def add(self, increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)


object1 = Myclass()
object1.add(5)
"""

"""
# Coding Challenge 12 (My Solution)
class Computer:

    def __init__(self, cpu, memory, disk, year):
        self.cpu = cpu
        self.memory = memory
        self.disk = disk
        self.year = year


    def getspecs(self):
        self.cpu = input("Enter Computer CPU Count: ")
        self.memory = input("Enter RAM size in GB: ")
        self.disk = input("Enter Total Disk Size in GB: ")
        self.year = input("Year Built: ")


    def displayspecs(self):
        print(self.cpu)
        print(self.memory)
        print(self.disk)
        print(self.year)


# computer1 = Computer("", "", "", "")
# computer1.getspecs()
# computer1.displayspecs()

class Desktop(Computer):

    def __init__(self, case):
        self.case = case

    def getdesktop(self):
        self.case = input("Enter The Case Type: ")

    def displaydesktop(self):
        print(self.case)

desktop1 = Desktop("")
desktop1.getspecs()
desktop1.getdesktop()
desktop1.displayspecs()
desktop1.displaydesktop()

# class Lpatop(Computer)
"""

"""
# Coding Challenge 12 (Given Solution)
class Computer:
    def __init__(self, ram, memory, processor):
        self.ram = ram
        self.memory = memory
        self.processor = processor

    def getspecs(self):
        print('Please enter the details')
        self.ram = input('Enter Ram Size')
        self.memory = input('Memory size')
        self.processor = input('Enter processor')

    def displayspecs(self):
        print('Here are the specs of the computer')
        print(' Ram size is: ' + self.ram + ' Memory size is: ' + self.memory + ' processor is: ' + self.processor)


class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor

    def get_case_details(self):
        self.casecolor = input('Enter case color')

    def put_case_details(self):
        print('case color is: ' + self.casecolor)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def getweight(self):
        self.weight = input('Enter weight')

    def displayweight(self):
        print('weight is: ' + self.weight)


comp = Laptop('');

comp.getspecs()

comp.getweight()

comp.displayspecs()

comp.displayweight()
"""


# Coding Challenge 13 (My Solution)
class Number:

    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x


print(Number(3) * Number(3))