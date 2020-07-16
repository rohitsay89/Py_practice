#!/usr/local/bin/python3.8
"""
Documentation for Python Basics
"""
# =============================================================#
import sys
import datetime
# =============================================================#

#==============================================================#
print("Hello World, this is python learning codebase")
print("Major version = ", sys.version_info.major,
      "\nMinor version = ", sys.version_info.minor)
print("Run Date & Time = ", datetime.datetime.now())
# =============================================================#

# Variables and Data Structures

# Assigning Integer
my_number = 4
print(my_number)

# Assigning float
your_number = 4.5

# Creating an empty list
numbers = []

# Appending data into the list
numbers.append(24)

# Appending string into the list
numbers.append("myname")

# Input from users from command line
name = input("Enter your name: ")

# Print input data
print("Greetings", name)

# Convert the input into integer
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

# Multiplying
number3 = number1 * number2
print("Product is :", number3)

# If statement
input_number = int(input("Enter your number : "))
if (input_number > 1):
    print("The number entered is greater than 1")
elif (input_number < 50):
    print("The number entered is less than 50")
elif (input_number > 50):
    print("The number entered in greater than 50")
else:
    print("Invalid number")


# Function
def greet(name):
    print("Hello", name)
    
greet('Dhee')

#===============================================================================#
# This program shows how to use input in python, find data type and typecasting
#===============================================================================#


# Input raw data from user
data = input("Enter anything : ")
print(data)

# Print the type of user input
print("The input data type is : ", type(data))

# Type casting user input

# Typecasting user input into integer
input1  = int(input("Enter a number : "))

# Typecasting user input into float 
input2  = float(input("Enter a float value : " ))

# Typecasting user input into string 
input3 = str(input("Enter a string : "))

print("####---Results---####")
print(f"The first input is  {input1} Type of input is {type(input1)}")
print(f"The second input is {input2} Type of input is {type(input2)}")
print(f"The second input is {input3} Type of input is {type(input3)}")

#==========================================================================#
# Multiple input using split()
#==========================================================================#
# Taking 2 inputs at a time
x, y = input("Enter two numbers : ").split()
print(f"value of {x} and value of {y}")

# Taking 2 comma separated inputs at a time  
x, y = input("Enter two numbers seprated by comma ',' : ").split(',')
print(f"value of {x} and value of {y}")

# Taking mutiple input at a time and putting into a list
x = list(map(int, input("Enter multiple values to put into an list : ").split()))
print("List of students : ", x)


# How to take multiple input using List comprehension
x, y = [int(x) for x in input("Enter two numbers : ").split()]
print(f"The first number {x} and second number is {y}")

#==========================================================================#
# Multiple input using split()
# print command syntex 
#==========================================================================#

#==================================================================================================================#
# Syntax: print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)
# Parameters:
# value(s) : Any value, and as many as you like. Will be converted to string before printed
# sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
# end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
# file : (Optional) An object with a write method. Default :sys.stdout
# flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False
# Returns: It returns output to the screen.
#==================================================================================================================#

print("The world is mine!!")

# Print line with comma in between
print("E","N","D", sep=',')

# Print line no space 
for i in range(5):
    print(i, end="")


for i in range(5):
    print(i, end="$")

#==================================================================================================================#
#OPERATOR	DESCRIPTION	SYNTAX
#+	Addition: adds two operands	x + y
#-	Subtraction: subtracts two operands	x - y
#*	Multiplication: multiplies two operands	x * y
#/	Division (float): divides the first operand by the second	x / y
#//	Division (floor): divides the first operand by the second	x // y
#%	Modulus: returns the remainder when first operand is divided by the second	x % y
#**	Power : Returns first raised to power second	x ** y
#==================================================================================================================#

a = 10 
b = 10
y = 35
z = 6

# Adding two numbers 
print("Sum of numbers : {a+b}")

# Subtraction 
print(a-b)

# Multiplication 
print(a*b)

# Division (float)
print(y/z)

# Division (floor)
print(y//z)

# Modulus 
print(y%z)

# Power 
print(a**b)

#========================================================================#
# Any and All operator in python
# Syntax : any(list of iterables)
#========================================================================#

# Since all are false, false is returned 
print(any ([False, False, False, False]))

# Here the method will short-circuit at the 
# second item (True) and will return True. 
print(any ([False, True, True, False, False]))

 
# Here the method will short-circuit at the 
# first (True) and will return True. 
print(any ([True, True, True]))

# Practical Example

list1 = []
list2 = []

for i in range(1,11):
    list1.append(4*i)

for i in range(0,10):
    list2.append(list1[i]%5 == 0)

print("Find if there is any number divisible by 5")
print(any(list2))
print(list2)


# All operator is True when all the inputs in the list are True

print(all([True, True, True, True, True]))
print(all([False, False, False, False, False]))

print(all([True, False, False, False]))


# Library to call operators
import operator

#==================================================================================================================#
# A string is a sequence of characters. 
# It can be declared in python by using double quotes. 
# Strings are immutable, i.e., they cannot be changed.
# Strings are immutable, i.e.  That can not be changed 
#==================================================================================================================#

a = "This is a string"

print(a)
#==================================================================================================================#
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
# '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
#  'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
#  'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
#  'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
#==================================================================================================================#
# Accessing values in a string
s = 'The world is awesome'

#==================================================================================================================#
# In Python, individual characters of a String can be accessed by using the method of Indexing. 
# Indexing allows negative address references to access characters from the back of the String,
# e.g. -1 refers to the last character, -2 refers to the second last character and so on.
# While accessing an index out of the range will cause an IndexError. Only Integers are 
# allowed to be passed as an index, float or other types will cause a TypeError.
#==================================================================================================================#
print("\nAccessing first character in a string")
print(s[0])

print("\nAccessing last character in a string")
print(s[-1])

# String Module


import string 
#==================================================================================================================#
#Help on module string:

#NAME
#   string - A collection of string constants.

#MODULE REFERENCE
#   https://docs.python.org/3.8/library/string
    
 #   The following documentation is automatically generated from the Python
 #   source files.  It may be incomplete, incorrect or include features that
 #   are considered implementation detail and may vary between Python
 #   implementations.  When in doubt, consult the module reference at the
 #   location listed above.

#DESCRIPTION
 #   Public module variables:
    
  #  whitespace -- a string containing all ASCII whitespace
  #  ascii_lowercase -- a string containing all ASCII lowercase letters
  #  ascii_uppercase -- a string containing all ASCII uppercase letters
  #  ascii_letters -- a string containing all ASCII letters
  #  digits -- a string containing all ASCII decimal digits
  #  hexdigits -- a string containing all ASCII hexadecimal digits
  #  octdigits -- a string containing all ASCII octal digits
  #  punctuation -- a string containing all ASCII punctuation characters
  #==================================================================================================================#

#==================================================================================================================#
# List in python 

# Lists are one of the most powerful tools in python. They are just like the arrays declared in other languages. 
# But the most powerful thing is that list need not be always homogenous. A single list can contain strings, 
# integers, as well as objects. Lists can also be used for implementing stacks and queues. Lists are mutable, i.e., 
# they can be altered once declared.
#==================================================================================================================#

# Declearing a list 
l = [1,3,5,6,67,'dhee', 'san francisco']
print(l)

#==================================================================================================================#
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', 
# '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 
# i 'reverse', 'sort']
#==================================================================================================================#

#==================================================================================================================#
# Tuples 

# A tuple is a sequence of immutable Python objects.
# Tuples are just like lists with the exception that tuples cannot be changed once declared. 
# Tuples are usually faster than lists
#==================================================================================================================#

# Declearing tuple 

t = (1, 2 ,4 ,5 ,6 ,6 , 'call', 'home', 'city')
print(t)


#==================================================================================================================#
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
# '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', 
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
#==================================================================================================================#

