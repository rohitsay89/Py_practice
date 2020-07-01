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
        if(self.employed == 'Y'):
            return "Employed"
        else:
            return "Not Employed"

#x = Student()
#x = GradStudent()
#print("Name = ", x.getName(), "Age = ", x.getAge())
#print("Roll number = ", x.getRollNumber(), "Average marks = ", x.getAvgMarks())
#print("Subject = ", x.getSubject(), "Employment status = ", x.getEmploymentStatus())

# iterators using classes
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if(self.index == 0):
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

#print("Iterators using a class")
#rev = Reverse('spam')
#iter(rev)
#for char in rev:
#    print(char)

# PRINT_LAST_K_LINES_IN_A_FILE, K = 5
# open a file in reading mode
def PRINT_LAST_K_LINES_IN_A_FILE(K):
    try:
        myFile = open("books.txt", "r")
        print(myFile)
        #print(myFile.read())
        #print("Tell = ", myFile.tell())
        #print("Seek = ", myFile.seek())
        count = 0
        for line in myFile:
            count = count + 1
        print("Number of lines = ",count)
        if(K > count):
            print("Printing all lines as requested value is more that number of lines in the file")

        # Move back the file pointer to start of file
        myFile.seek(0,0)

        lineCount = 0
        for line in myFile:
            # skip the lines which are less than count-K
            if(lineCount >= count-K):
                print(line)
            lineCount = lineCount + 1
        myFile.close()

    except:
        print(sys.exc_info())

#print("PRINT_LAST_K_LINES_IN_A_FILE")
#PRINT_LAST_K_LINES_IN_A_FILE(5)
#PRINT_LAST_K_LINES_IN_A_FILE(23)

# Read a binary file
def ReadBinFile():
    try:
        myBinFile = open("test_boot.bin", "rb")
        myBinFile.read()
        print("Length = ", myBinFile.tell(), "Bytes")
        # set the file pointer back to origin
        myBinFile.seek(0,0)

        myBinFile.close()

    except:
        print(sys.exc_info())

print("This is binary file read snippet")
ReadBinFile()