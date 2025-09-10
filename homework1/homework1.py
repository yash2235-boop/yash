

# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print (b)
print(type(b)) # b is a float, a number with a decimal

c = 3j
print (c)
print (type(c)) #c is a complex data type which contains a number and an alphabet. 
# A complex data type is one that is made up of other existing data types 
# (string and int in this case)

d = "hello"
print(d)
print(type(d)) # d is a string, a data type containing alphabets

e = [1,2,3]
print (e)
print(type(e)) # e is a list, which contains multiple int in one variable

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dict, which is a data type that contains a collection of key-value pairs.

g = (1, 2)
print (g)
print(type(g)) #g is a tuple. It is an ordered collection of items. It is like a list but it cannot be changed.

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) #h is a list which contains multiple strings in one variable

i = True
print (i)
print(type(i)) # i is a boolean which holds a value of either True or False

j = None
print(j)
print(type(j)) #j is a NoneType, which represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) #k is a list which contains a string, boolean value and an integer in one variable

l = str(14)
print(l)
print(type(l)) # l is a string, a data type containing alphabets

m = 1e4
print(m)
print(type(m)) #m is a float which is written in scientific notation

#Questions:
# How many different data types did you find?
# I found 9 data types

# List all the data types you found.
#int, str, list, float, dict, tuple, complex, bool, nonetype

#What variables have the same data types?
#int - a
#str - d, l
#list - e, h ,k
#float - b, m
#dict - f
#tuple - g
#complex - c
#bool - i
#nonetype - j

#What was the data type of l? Why is it not an integer? What does str() do?
#l is a string. It is not an integer as the function str() converts it into a string. Str() converrts a value in the brackets into a string.

#Look up one more data type not given above. Repeat the same procedure.
n = {1,2,3,3}
print (n)
print(type(n)) # n is a set which is an unordered collection of unique items.


# --- Booleans ---
print(10 > 9) # True, 10 is greater than 9
print(10 == 9) #False, 10 is not equal to 9
print (10 <= 9) #False, 10 is not less than or equal to 9
print(bool("abc")) # True, non-empty strings evaluate to true in python
print(bool(123)) #True, any nonzero number returns True
print(bool(["apple", "cherry", "banana"])) # True, non empty lists return true
print(bool(True)) #True, it is explicitly true
print(bool(False)) #False, explicitily false
print(bool(0)) # False, 0 is considered false in python
print(bool("")) #False, the string is empty which is false
print(bool(" ")) #True, the space counts as a character in the string
print(bool(())) #False, empty tuple is false 
print(bool([])) # False, empty list is false
print(bool({})) # False, empty dictionary is false

# Questions:
# What pattern do you notice about expressions returning True or False?
# Most expressions that return false either have a 0 or are empty.

# Which expression surprised you about its result?
# print(bool(" ")) - I did not know a space counts as a character

# Create an expression, not given above, that will return True. Why is it True?
# print (bool([0])) - This will be true cause the list is not empty, even when it contains a 0

# Create an expression, not given above, that will return False. Why is it False?
#print(bool(None)) None returns false in python

#--- Operators ---
# --- 3.3.1: Arithmetic Operators ---
print(10 + 5)   # 15 - additions
print(10 - 5)   # 5 - subtraction
print(2 * 4)    # 8 - multiplication
print(6 / 3)    # 2.0 - division converts to a float
print(5 % 2)    # 1 - modulus - gives the remainder
print(3 ** 2)   # 9 - puts the number after ** in the power/ exponent
print(15 // 2)  # 7 - floor division - gives the quotient without remainder 

# --- 3.3.2: Comparison Operators ---
print(5 == 2) # False, 5 is not equal to 2
print(10 != 10) # False, 10 is not not equal to 10
print(2 < 5) #True, 2 is lesser than 5
print(12 > 5) #True, 12 is greater than 5
print(5 <= 6) #True, 5 is lesser than or equal to 6
print(1 >= 10) #False, 1 is not greater than or equal to 10

# --- 3.3.3:  Assignments Operators ---
x = 5
x += 5 # 10, adds 5 to x and reassigns it back to x: x = x+5
print (x)
x -= 4 # 6, subtracts 4 from 10 (new value of x) and reassigns it: x = x - 4
print(x)
x*= 3 # 18, multiplies 6 by 3 and reassigns to x : x = x * 3
print(x)

# --- 3.3.4: Logical Operator ---
# 1. The operator 'and' returns True only if both conditions are True.\
# 5 > 2 and 10 > 3 - True
# 5 > 2 and 10 < 3 - False

# 2. The operator 'or' returns True if at least one condition is True.
# 5 > 2 or 10 < 3 - True
# 2 > 5 or 3 > 10 - False

# 3. The operator 'not' reverses the Boolean value.
# not (5 > 10) - True
# not (5 < 10) - False

# More questions
# What is the difference between / and //?
# / is a dividing operator which returns a float,
#  whereas //does floor divison which returns an integer

#What is the difference between % and //?
# % is the modulus which returns the remainder after the division. // returns the quotient 
#without the remainder

#What operator would you use to calculate the remainder when dividing two numbers? Give
#an example.
# The modulus opeator - %: print (10 % 3) - returns 1

#How do assignment operators work?
#They work from right to left. They assign or update 
# the value on the right to the variable or other data types like lists... on the left


# --- Strings ---
my_string = "hello"

print(my_string) # Prints: hello

print(my_string[0]) # Prints: h  (first character)
print(my_string[1]) # Prints: e  (second character)
print(my_string[2]) # Prints: l  (third character)
print(my_string[3]) # Prints: l  (fourth character)
print(my_string[4]) # Prints: o  (fifth character)
print(my_string[-1]) # Prints: o  (last character, negative index counts backwards)
print(my_string[1:3]) # Prints: el (characters from index 1 up to but not including 3)
print(my_string[0:5:2]) # Prints: hlo (characters from start to 5, stepping by 2)
print(len(my_string)) # Prints: 5 (length of the string)
print(my_string + "goodbye") # Prints: hellogoodbye (combination of two strings)
print(my_string * 7) # Prints: hellohellohellohellohellohellohello (repetition)

# Questions
#Define the term slicing. For which of the manipulations did you slice your string?
# Slicing is process of extracting some portions of a string using the format: 
#[start:stop:step]
#We used slicing in print(my_string[1:3]) and print(my_string[0:5:2]) 

name = 'Oski'
print("Hello, my name is", name) #the comma in the print function
#adds a space and it combines the string with the varriable

name = "Oski"
print(f"Hello, my name is {name}") # the f makes it a formatted string. 
#{name} is directly replaced with the value of the variable name

#What is the difference between the two last print statements?
#The first statement uses a comma for a separation which adds a space in between the items.
#The second statement uses a formatted string which allows us to embed variables 
#and expressions directly inside the string.
#It gives us more flexibility in cases where we need to round off numbers

# --- Terminal Commands ---
# 1. cd
# Changes directory. Use to move between folders.
# Example: cd Documents

# 2. ls
# Lists files and directories in the current folder.
# Example: ls

# 3. ls -a
# Lists all files, including hidden ones (those starting with ".").
# Example: ls -a

# 4. mkdir
# Creates a new directory (folder).
# Example: mkdir yash_new_folder

# 5. cat
# Displays the contents of a file in the terminal. Stands for concatenate
# Example: cat file.txt

# 6. pwd
# Prints the current working directory.
# Example: pwd

# 7. cd ..
# Goes to the parent directory.
# Example: cd ..

# 8. cd .
# Stays in the current directory (no movement, rarely used).
# Example: cd .

# 9. cd ~
# Moves to the home directory.
# Example: cd ~

# 10. cp
# Copies files or directories.
# Example: cp file.txt backup.txt this copies the file file.txt and creates a new file named
# backup.txt in the same directory

# 11. mv
# Moves or renames files and directories.
# Example: mv oldname.txt newname.txt

# 12. rm
# Deletes files 
# Example: rm file.txt

# 13. clear
# Clears the terminal screen.
# Example: clear

# 14. grep
# Searches for specific text inside files.
# Example: grep "hello" file.txt

#Questions
# Look up 3 other commands not present. Define and explain how to use them on the command line

# touch - creates an empty file
# Example: touch notes.txt

# head - displays the first few lines of a file (shows first 10 lines by default)
# Example: - head file.txt

# tail - displays the last few lines of a file (shows last 10 lines by default)
# Example: - tail file.txt

# What is the difference between ls and ls -a?
# ls only shows visible files and folders whereas ls -a shows all files including hidden files
# like those starting with a . (.py etc)

# What is a hidden file?
# A hidden file is one that ends with a dot. example - script.py

# Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to
# use them on the command line.
# ls -l: lists files in a long format (shows size, permissions, owner) example: ls -l
# ls -h: displays files in human - readable format (MB, KB) example: ls -lh
# ls -R: lists files recurrsively, showing files inside subdirectories example: ls -R
