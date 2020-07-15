# This is a python file for using implementing basic data structures using python
# =============================================================#
import sys
import datetime
"""
1. Stack 
2. Queue 
3. Circular queue
4. Tree
5. Graph
"""
# =============================================================#
print("Hello World, this is Data Structure in python implementation")
print("Major version = ", sys.version_info.major,
      "\nMinor version = ", sys.version_info.minor)
print("Run Date & Time = ", datetime.datetime.now())

# =============================================================#

# Program to create a stack data structure in Python using list
a = [0, 0, 0, 0, 0]  # create a default list of all zeros
top = 0
print("Program to create a stack data structure in Python using list \n")


def Push(n):  # Push function: Push data on the stack
    global top  # specify the 'top' variable is global
    a[top] = n  # store the value at the top of stack
    top = top + 1  # increment the top
    print("Top = ", top)  # print the top position number after each Push operation


def Pop():  # Pop function: remove data from top of stack
    global top  # specify the 'top' variable is global
    top = top - 1  # decrement the top variable
    print("Top = ", top)  # print the top position number after each Push operation


def learnStack():
    print(a)
    Push(5)  # Push and Pop operation
    Push(6)
    Push(27)
    Pop()
    Pop()
    print(a)  # Print the updated list after all operations


# ============================================================#

learnStack()

