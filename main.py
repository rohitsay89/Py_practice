import sys
import datetime

print("Hello World, this is python learning codebase")
print("Major version = ", sys.version_info.major,
      "\nMinor version = ", sys.version_info.minor)
print("Run Date & Time = ", datetime.datetime.now())

# simple function implementation:
def add_func(x, y):
    print("This is a function for adding 2 nums")
    z = x+y
    print("Sum = ", z)
#add_func(20, 20)
print("Scope name = ", __name__)

# Sample Base class
class Person:
    # Base class constructor:
    def __init__(self):
        self.name = input("Enter First name:")
        self.age = input("Enter Age:")
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

# Sample Derived class
class Student(Person):
    # Derived class constructor:
    def __init__(self):
        Person.__init__(self)
        self.rollNum = input("Enter Roll number:")
        self.avgMarks = input("Enter average marks:")
    def getRollNumber(self):
        return self.rollNum
    def getAvgMarks(self):
        return self.avgMarks

x = Student()
print("Name = ", x.getName(), "Age = ", x.getAge())
print("Roll number = ", x.getRollNumber(), "Average marks = ", x.getAvgMarks())
