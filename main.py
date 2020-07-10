# =============================================================#
import sys
import binascii
import datetime

# =============================================================#
print("Hello World, this is python learning codebase")
print("Major version = ", sys.version_info.major,
      "\nMinor version = ", sys.version_info.minor)
print("Run Date & Time = ", datetime.datetime.now())
# print("Scope name = ", __name__)

# =============================================================#

# Python Calculator:
def add_func(x, y):
    # print(x+y)
    return (x + y)


def mul_func(a, b):
    # print(a*b)
    return (a * b)


# this division will return result as float
def div_float(a, b):
    # print(a/b)
    return (a / b)


# this division will return integer part of result
def div_int(a, b):
    # print(a//b)
    return (a // b)


def div_mod(a, b):
    # print(a%b)
    return (a % b)


def num_power(a, p):
    # print(a**p)
    return (a ** p)



# PRINT_LAST_K_LINES_IN_A_TEXT_FILE, K = 5
# open a file in reading mode
def PRINT_LAST_K_LINES_IN_A_FILE(K):
    try:
        myFile = open("books.txt", "r")
        print(myFile)
        # print(myFile.read())
        # print("Tell = ", myFile.tell())
        # print("Seek = ", myFile.seek())
        count = 0
        for line in myFile:
            count = count + 1
        print("Number of lines = ", count)
        if (K > count):
            print("Printing all lines as requested value is more that number of lines in the file")

        # Move back the file pointer to start of file
        myFile.seek(0, 0)

        lineCount = 0
        for line in myFile:
            # skip the lines which are less than count-K
            if (lineCount >= count - K):
                print(line)
            lineCount = lineCount + 1
        myFile.close()

    except:
        print(sys.exc_info())
    finally:
        print("This is finally clause")


# print("PRINT_LAST_K_LINES_IN_A_FILE")
# PRINT_LAST_K_LINES_IN_A_FILE(5)
# PRINT_LAST_K_LINES_IN_A_FILE(23)

# =============================================================#
# Read a binary file
def ReadBinFile(K):
    print("This is binary file read snippet")
    try:
        # myBinFile = open("test_boot.bin", "rb")
        with open("test_boot.bin", "rb") as myBinFile:

            # get the size of binary file in bytes
            myBinFile.read()
            binFileSize = 0
            print("Length = ", myBinFile.tell(), "Bytes")
            binFileSize = myBinFile.tell()
            if (K > binFileSize):
                print("Requested bytes are larger than file size printing all bytes")

            # set the file pointer back to origin
            myBinFile.seek(0, 0)

            # now read first 20 bytes and print them
            data = myBinFile.read(20)
            hex_data = binascii.hexlify(data)

            # reset the file pointer back to start location
            myBinFile.seek(0, 0)

            print("Printing first", K, "Bytes of the bin file")
            # for count in range(binFileSize):
            for count in range(K):
                print(binascii.hexlify(myBinFile.read(1)), count)

            myBinFile.close()
    except:
        print(sys.exc_info())
    finally:
        print("This is finally clause")


# =============================================================#

def addressOfObjects():
    x = 10
    y = 20
    print("Address of x = ", id(x))
    print("Address of Y = ", id(y))
    a = GradStudent()
    print("Address of A = ", id(a))


# =============================================================#

def pythonCalculator():
    a = 10
    b = 20
    print("Addition: ", add_func(a, b))
    print("Multiplication: ", mul_func(a, b))
    print("Float division: ", div_float(a, b))
    print("Integer part division: ", div_int(a, b))
    print("Modulus operation: ", div_mod(a, b))
    print("Exponent: ", num_power(a, b))


# =============================================================#

# lists are 0 indexed, i.e. they start from 0,1,2,3,4.....n
def learnLists():
    print("This is List example snippet")
    try:
        squares = [1, 4, 9, 16, 25]
        # print(squares)

        # print from 1st element to last, not including 0th element
        # print(squares[1:])

        # concatinate squares:
        squares = squares + [36, 49, 64, 81, 100]
        # print(squares)

        # can access individual element of the list
        squares[0] = 2
        # print(squares)

        # can print lenght using len
        # print(len(squares))

        print("Create list of squares of first 10 numbers")
        # empty the list
        squares = []
        var = []
        for num in range(1, 11):
            # print("Num = ", num)
            squares = squares + [num_power(num, 2)]
        print(squares)
    except:
        print(sys.exc_info())


# =============================================================#


# ReadBinFile(20)
# addressOfObjects()
# pythonCalculator()
learnLists()

# =============================================================#
