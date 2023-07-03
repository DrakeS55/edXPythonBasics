# create a list
L = ["Michael Jackson", 10.1, 1982]
L

# Print the elements on each index
print("positive:", L[0], "\n" "negative:", L[-3])
print("positive:", L[1], "\n" "negative:", L[-2])
print("positive:", L[2], "\n" "negative:", L[-1])

# we can nest lists / tuples within each other
# example nested list
sampleList = ["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]
sampleList

# can also perform slicing using lists
# want last two variables in list
L
L[1:]

# can use extend() method to add elements to a list
L
L.extend(["MJ", 1975])
L

# can also use append() method. This will add just one element to the list (i.e., you will add a nested list into the original list)
L.append(["MJ2", 1956])
L

# Lists are MUTABLE, meaning we can change them
# I can change the first variable of the List as such
L
L[0] = "test" # replaces the variable in the first position with "test"
L

# can also delete an element in a list using the del() command
print("Before deletion:", L)
del(L[0])
print("After Deletion:", L)

# can use split() method to split a string components into a list. Default method is to separate via spaces
"hard rock".split()

# split the string by comma (delimiter) - pass as argument into split() method
"A,B,C".split(",")

# Copy / Clone lists
# Copy (copy by reference) List A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Examine the copy by reference 
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# because of the "copy by reference", List B has also changed along with List A. This is because they SHARE the same object in memory

# You can clone List A via the following syntax
A
B = A[:]
B
# this forces B to see a new object in memory. So, you will not have the unforseen side effect that we saw with the "copy by reference" method above

# examine new copy of List A
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])
# because B sees a new list in memory, it still shows the original first variable, not the new variable that we changed in list A

#  QUIZ

# create list a_list with following elements: 1, hello, [1,2,3], and True
a_list = [1, "hello", [1,2,3], True]
a_list

# find the value stored at index 1 of a_list
print(a_list[1])

# retrieve elements stored in index 1, 2, and 3 of a_list
a_list[1:4]

# concatenate the following lists
A = [1, 'a']
B = [2, 1, 'd']
A+B

# SCENARIO - Create a shopping list

# TASK 1 - Create an empty list
ShoppingList = []

# TASK 2 - store items in empty list
ShoppingList.extend(["Watch", "Laptop", "Shoes", "Pen", "Clothes"])
ShoppingList

# TASK 3 - Add new item in shopping list - football
ShoppingList.extend(["Football"])
ShoppingList

# TASK 4 - Print first item in shopping list
print(ShoppingList[0])

# TASK 5 - Print Last item in shopping list
print("postive indexing:", ShoppingList[5], "\n", "negative indexing:", ShoppingList[-1])

# TASK 6 - Print Entire Shopping List
print(ShoppingList[:])

# TASK 7 - print important items. Laptop and shoes
ShoppingList[1:3]

# TASK 8 - Change item in shopping list. Change pen to notebook
ShoppingList[3] = "Notebook"
ShoppingList

# TASK 9 - Delete uneccesary item. Delete Clothes
del(ShoppingList[4])
ShoppingList

# TASK 10 - print the shopping list
print(ShoppingList)
ShoppingList