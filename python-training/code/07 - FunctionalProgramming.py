"""
# Functional Programming
def add_ten(x):
    return x + 10

def twice(func, arg):
    return func(func(arg))

print(twice(add_ten, 10))
"""

"""
# Lambdas
def square(x):
    return x ** 2


print(square(4))
print((lambda x: x ** 2)(30))
"""

"""
# Map Function
def add(x):
    return x + 2


def multiply(x):
    return x * 2


newlist = [10, 20, 30, 40, 50]

print(list(map(add, newlist)))
print(list(map(lambda x: x + 2, newlist)))
print(list(map(multiply, newlist)))
print(list(map(lambda x: x * 2, newlist)))
"""

"""
# Filters
newlist = [1, 3, 4, 5, 7, 2, 9, 11, 13]

result = list(filter(lambda x: x % 2 == 0, newlist))
print(result)
"""

"""
# Generators
def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1


for x in function():
    print(x)


def even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(even_numbers(21)))
"""

"""
# Coding Challenge 9 (My Solution)
def student_discount(x):
    return x * .1

def customer_discount(x):
    return x * .05

cost = 100
result = cost - customer_discount(cost) - student_discount(cost)
print(result)
"""

"""
# Coding Challenge 9 (Given Solution)
def student_discount(price):
    price = price - (price * 10) / 100
    return price


def additional_discount(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice


selling_price = 100

# applying both discounts simultaneously

print(additional_discount(student_discount(selling_price)))
"""

"""
# Coding Challenge 10 (My Soltuion)
print((lambda x: x * (x + 5) ** 2)(5))

# Coding Challenge 10 (Given Solution)
result = (lambda x: x*(x+5)**2)(5)
print(result)
"""


# Coding Challenge 11 (My Solution)
def discount(x):
    return x * .9


products = [100, 200, 300, 400, 500]

print(list(map(discount, products)))
print(list(map(lambda x: x * .9, products)))


# Coding Challenge 11 (Given Solution)
def discount(price):
    price = price - (price * 10) / 100
    return price


product_prices = [100, 200, 300, 400, 500]

updated_prices = list(map(discount, product_prices))

print(updated_prices)