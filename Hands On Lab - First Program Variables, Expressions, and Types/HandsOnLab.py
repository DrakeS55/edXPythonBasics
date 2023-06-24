# Say Hello to Python
print("Hello Python!")

# Check the Python Version
import sys
print(sys.version)

# Print string as error message
# frint("Hello Python!")
print("Hello Python!")

# Print String and error to see the running order
print("This will be printed")
# frint("This will cause an error")
print("This will cause an error")
print("This will be printed")

# Exercise - your first program: print "Hello, World"
print("Hello, World") # print the traditional hello, world

# Python Types Exercises

# integer (int)
12

# float (decimal)
12.0

# string (str)
"This is a string"

# Can use the type() function to check the type of a given variable
# check the type of 12.0 (should be float)
type(12.0)

# learn more about the specifics of float numbers
sys.float_info
# gives max and min float values

# typecasting - changing object types in Python

# verify that this is an integer
type(2)

# typecast int to float
float(2)

# convert int 2 to float 2 and check type - should be a float
type(float(2))

# typecasting int to float is OK
# typecasting float to int can make you lose information (lose decimal information)
# typecast 3.55 to 3 using int(3.55) - should read "3"
int(3.55)
# check type to ensure that the float was converted to int
type(int(3.55))

# Boolean Types - True or False
# Value True
True
# Value False
False

# Type of True and False - should be "bool"
type(True)
type(False)

# Exercises - Types

# what is data type of 6 / 2 - should be float
6 / 2
# \ division ALWAYS results in a float data type
# use \\ to result in int type
6 // 2
# this should read "3", which is an integer type

# Exercise - Expressions

# write expression that calculates the number of hours in 160 min
min = 160 # num. minutes
min / 60 # float division to get number of hours with decimal - not going to be a round number

# Mathematical expression
30 + 2 * 60

# store value into variable
x = 43 + 60 + 16 + 41

# print out the value in a variable
x

# Use another variable to store the result of an operation between variable and value
y = x / 60
y

# Name the variables meaningfully
total_min = 43 + 42 + 57 # total length of albums in min
total_min

# expression to determine hours from total minutes
total_hours = total_min / 60
total_hours

# Exercise: Expression and Variables in Python
x = 3 + 2 * 2
x

y = (3 + 2) * 2
y

z = x + y
z