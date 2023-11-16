import random
5  # Integer

3.14  # Float

"Hello World"  # String
'Also a string'

True  # Boolean
False

None  # NoneType

# Variables
# Variable names can contain letters, numbers, and underscores
# They cannot start with a number
# They are case sensitive
# They cannot be a reserved word
# Reserved words include:
# and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield

# Variable assignment
x = 5
y = 3.14
z = "Hello World"

# Variable reassignment
x = 6
y = "Changed"
z = 3.14

# Variable assignment with multiple variables
x, y, z = 5, 3.14, "Hello World"

# Variable assignment with one value to multiple variables
x = y = z = "Same value"

# Arithmetic Operators
addition = 10 + 10
print(addition)

subtraction = 10 - 10
print(subtraction)

multiplication = 50 * 5
print(multiplication)

division = 50 / 5
print(division)

modulus = 51 % 2
print(modulus)

exponentiation = 5 ** 5
print(exponentiation)

floor_division = 50 // 20
print(floor_division)

# Assignment Operators
x = 5

x += 5
print(x)

x -= 5
print(x)

x *= 5
print(x)

x /= 5
print(x)

x %= 5
print(x)

x **= 5
print(x)

x //= 5
print(x)


# f string formatting
university = "King's College London"
country = "United Kingdom"

print(f"{university} is in {country}")

# User Input
campus = input("On what campus are you based? ")

# Data type conversion
pi = input("What is the value of pi? ")

pi = float(pi)

# Conditionals
# if, elif, else

# Comparison Operators
# ==, !=, >, <, >=, <=

x = 3
y = 5

print(x == y)

print(x != y)

print(x > y)

print(x < y)

print(x >= y)

print(x <= y)

# Logical Operators
# and, or, not

x = 3
y = 5

print(x == 3 and y == 5)

print(x == 3 or y == 5)

print(not x == 3)

# Loops and recursion
# for, while

# for loop
for i in range(5):
    print(i)

# while loop
i = 0
while i < 5:
    print(i)
    i += 1

# Breaks and continues

# break
for i in range(5):
    if i == 3:
        break
    print(i)

# continue
for i in range(5):
    if i == 3:
        continue
    print(i)

# Random

# Random integer
print(random.randint(0, 10))

# Naming conventions
snake_case
# To be used for variable names

CamelCase
# To be used for class names

kebab-case
# To be used for file names

# Comments
# Single line comment

"""
Multi
Line
Comment
"""
