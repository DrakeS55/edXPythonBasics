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
# define the pattern to search for
pattern = r"Jackson"
# use the search() method to search for the pattern in the string
result = re.search(pattern, s1)
# check if a match was found
print(result)

# Using Special Sequences
# \d
pattern = r"\d\d\d\d\d\d\d\d\d\d" # Mathces any 10 consecutive digits
text = "My phone number is 1234567890"
match = re.search(pattern, text)
match

# \W
pattern = r"\W" # Matches any non word character
text = "Hello, World!"
matches = re.findall(pattern, text)
print("Matches:", matches)

# findall() method finds all occurrences of a specified pattern within a string
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
# use the findall() method to find all occurrences of "as" in the string
result = re.findall("as", s2)
print(result)

# RegEx split() function splits a string into an array of substrings based on a specified pattern
# Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)

# RegEx sub() function used to replace all occurrences of a pattern in a string with a specified replacement
# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string)

# QUIZ
# use slicing to print out the first 3 elements
d = "ABCDEFG"
print(d[0:3])

# use stride to print out every 2nd character
e = 'clocrkr1e1c1t'
print(e[::2])

# print out a backslash
print("\\")

# consider the variable g and find the first index of the sub-string "snow"
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \n Its fleece was white as snow And everywhere that Mary went Mary went, \n Mary went Everywhere that Mary went The lamb was sure to go"
print(g)

# to find first index, we can use find() method
snow_index = g.find("snow")
print(snow_index)

# in the variable g, replace "Mary" with "Rob"
replacement = "Rob"
print(g.replace("Mary", "Rob"))

# in the variable g, replace "," with "."
replacement = "."
print(g.replace(",", "."))

# split g to a list
print(g.split())

# in string s3, find consecutive digits using \d
s3 = "House number- 1105"
consec_digits = r"\d\d\d\d"
print(re.search(consec_digits, s3))
