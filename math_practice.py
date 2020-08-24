# This file is for simple math calculation scripts
import sys

step_count = 0

def fibonacci(n):
#using recursion
    #if(n <= 1):
    #    return n;
    #return fibonacci(n-1) + fibonacci(n-2)
# using for loop
    prev = 0
    current = 1
    next = 0
    print("Get size of next = ", sys.getsizeof(next))

    #print(prev, '\n', current)
    for i in range(1,n):
        next = prev + current
        #print(next)
        prev = current
        current = next
    print("Get size of next = ", sys.getsizeof(next))
    return next

# print values from 0 to (2^n - 1)
def twon_one(n):
    for i in range(0, n):
        y = ((2**i) - 1)
        print(i, y)


# Collatz conjecture
def threen_plus_one(x):
    if(x == 0):
        return -1
    global step_count
    step_count = step_count + 1
    #print('Number is = ', x)
    if (x % 2) == 0:
        y = x/2
        if y == 1:
            #print('\n\nEnd of test, number = 1, \nSteps taken = ', step_count)
            return int(step_count)
        else:
            return threen_plus_one(y)
    else:
        y = ((3*x) + 1)
        return threen_plus_one(y)

def calcPi():
    print(22/7)

def testCollatzConj(n):
    for i in range(1, n):
        print(i, threen_plus_one(i))



#twon_one(50)
#testCollatzConj(1000)
#calcPi()
#print("max size = ", sys.maxsize)
print(fibonacci(3000000))

