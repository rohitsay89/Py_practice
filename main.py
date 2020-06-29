import sys
import datetime

print("Hello World, this is python learning codebase")
print("Major version = ", sys.version_info.major,
      "\nMinor version = ", sys.version_info.minor)
print("Date & Time = ", datetime.datetime.now())

def add_func(x, y):
    print("This is a function for adding 2 nums")
    #x = 10
    #y = 20
    z = x+y
    print("Sum = ", z)

add_func(20, 20)