"""
# Try, Except, Finally Block
try:
    a = 20
    b = 0
    print(a / b)
except ZeroDivisionError:
    print('There is a divide by zero error')
finally:
    print('This is going to execute no matter what')
"""

"""
# File Writing
file = open("demo.txt", 'w')
file.write("This is the text written to the file")
file.close()

# File Reading
file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()

# File Appending
file = open("demo.txt", 'a')
file.write("\nThis is the new line")
file.close()
"""

"""
# Coding Challenge 5
def divide_numbers(a, b):
    try:
        result = str(a / b)
    except ZeroDivisionError:
        result = "Error: Division by Zero"
    finally:
        return result

print(divide_numbers(10, 3))


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("There is a divide by zero error")
        return 0


x = float(input('Enter a number'))
y = float(input('Enter value by which you want to divide the number'))
result = divide(x, y)
print(result)
"""


# Coding Challenge 6
file = open("demo.txt", 'w')
file.write("some data")
file.close()

file = open("demo.txt", 'r')
contents = file.read()
print(contents)
file.close()

file = open("demo.txt", 'a')
file.write("\nnew line")
file.close()