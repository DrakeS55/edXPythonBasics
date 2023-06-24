# Hands On Lab for Strings

name = "Michael Jackson"
name

# print the first element in the string
print(name[0])

# print the 6th element in the string
print(name[6])

# print the last element in the string using negative indexing
print(name[-1])
# negative indexing allows you to determine the final value in a string when the string length isn't known

# Find the length of the string
print(len(name))

# can also use slicing to obtain multiple characters from a string
# take the slice from index 0 to index 3
print(name[0:4])

# take the slice from index 8 to index 11
print(name[8:12])

# stride allows us to choose every "nth" variable within a string

# get every 2nd element. Elements on indexing 1, 3, 5, etc...
print(name[::2])

# we can use slicing along with stride
print(name[0:5:2]) # from index 0 to index 4, every 2nd letter

# concatenate, or add, strings together using +
statement = name + " is the best"
statement

# we can replicate string values by using *
3 * statement

# create new string via concatenation
name
statement
name = name + statement
name

# \ is used as "escape sequences" for strings. Can perform several functions

# \n is a new line
print("Michael Jackson is \n the best")

# \t represents a tab
print("Michael Jackson is \t the best")

# if you want to place a \ in the string, use \\
print("Michael Jackson is \\ the best")

# String Operations
# upper() method - convert all lowercase values to uppercase
a = "Thriller is his sixth studio album"
print("before upper:", a)
b = a.upper()
print("after upper:", b)

# lower() method - opposite of upper() method
a = "MICHAEL JACKSON IS FINE"
print("before lower:", a)
b = a.lower()
print("after lower:", b)

# replace() method replaces a substring with a new string
a = "Michael Jackson is the best"
print("before replace:", a)
b = a.replace("Michael", "Janet")
print("after replace:", b)

# find() finds a substring and outputs the first index number of the sequence
name = "Michael Jackson"
name.find("el")
name.find("Jack")
name.find('jack') # case sensitive, sense the substring "jack" isn't found (j is lowercase, not uppercase), a -1 is returned

# split() method splits a string at the specified separator and returns a list
split_string = name.split()
split_string

# RegX - Short for "regular expression", a python tool for matching and handling strings
import re # import tool

# search function searches for specified patterns within a string
s1 = "Michael Jackson is the best"

