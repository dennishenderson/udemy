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
