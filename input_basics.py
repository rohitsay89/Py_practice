#!/usr/local/bin/python3.8 

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

