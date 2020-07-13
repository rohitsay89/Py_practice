# =============================================================#
import sys
import datetime

# =============================================================#
print("Hello World, this is python learning codebase")
print("Major version = ", sys.version_info.major,
      "\nMinor version = ", sys.version_info.minor)
print("Run Date & Time = ", datetime.datetime.now())

# =============================================================#
# Sample Base class
class Person:
    # Base class constructor:
    def __init__(self):
        self.name = input("Enter First name: ")
        self.age = input("Enter Age: ")

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


# Sample Derived class
class Student(Person):
    # Derived class constructor:
    def __init__(self):
        Person.__init__(self)
        self.rollNum = input("Enter Roll number: ")
        self.avgMarks = input("Enter average marks: ")

    def getRollNumber(self):
        return self.rollNum

    def getAvgMarks(self):
        return self.avgMarks


class GradStudent(Student):
    def __init__(self):
        Student.__init__(self)
        self.subject = input("Enter Graduate coursename: ")
        self.employed = input("Enter employment status Y/N: ")

    def getSubject(self):
        return self.subject

    def getEmploymentStatus(self):
        if (self.employed == 'Y'):
            return "Employed"
        else:
            return "Not Employed"


def learnInheritance():
    print("Class demo")
    x = GradStudent()
    print("Name = ", x.getName(), "Age = ", x.getAge())
    print("Roll number = ", x.getRollNumber(), "Average marks = ", x.getAvgMarks())
    print("Subject = ", x.getSubject(), "Employment status = ", x.getEmploymentStatus())


# =============================================================#

# iterators using classes
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if (self.index == 0):
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


def learnClassIterators():
    print("Iterators using a class")
    rev = Reverse('spam')
    iter(rev)
    for char in rev:
        print(char)

# =============================================================#

def addressOfObjects():
    x = 10
    y = 20
    print("Address of x = ", id(x))
    print("Address of Y = ", id(y))
    a = GradStudent()
    print("Address of A = ", id(a))

# =============================================================#

learnInheritance()
#learnClassIterators()
#addressOfObjects()