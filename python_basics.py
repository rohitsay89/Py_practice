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

x, y = input("Enter two numbers : ").split()
print(f"value of {x} and value of {y}")