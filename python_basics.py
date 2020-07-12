#!/usr/local/bin/python3.8
"""
Documentation for Python Basics
"""
# =============================================================#
import sys
import datetime

# =============================================================#

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

Syntax: print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

Parameters:
value(s) : Any value, and as many as you like. Will be converted to string before printed
sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
file : (Optional) An object with a write method. Default :sys.stdout
flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

Returns: It returns output to the screen.


print("The world is mine!!")

# Print line with comma in between
print("E","N","D", sep=',')

# Print line no space 
for i in range(5):
    print(i, end="")


for i in range(5):
    print(i, end="$")

"""
OPERATOR	DESCRIPTION	SYNTAX
+	Addition: adds two operands	x + y
-	Subtraction: subtracts two operands	x - y
*	Multiplication: multiplies two operands	x * y
/	Division (float): divides the first operand by the second	x / y
//	Division (floor): divides the first operand by the second	x // y
%	Modulus: returns the remainder when first operand is divided by the second	x % y
**	Power : Returns first raised to power second	x ** y
"""

a = 10 
b = 10
y = 35
z = 6

# Adding two numbers 
print ("Sum of numbers : {a+b}")

# Subtraction 
print (a-b)

# Multiplication 
print (a*b)

# Division (float)
print (y/z)

# Division (floor)
print (y//z)

# Modulus 
print (y%z)

# Power 
print (a**)