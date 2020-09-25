# This file is for simple math calculation scripts
import sys
import math
import matplotlib.pyplot as plt

step_count = 0

import random

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


def summation():
    inputCurrent = []
    for t in range(0,3601):
        #print(t)
        inputCurrent = inputCurrent + [random.randint(41,49)]
    AHbat = 0
    for t in range(1, 3601):
        #print(t, AHbat)
        AHbat = AHbat + inputCurrent[t]

    AHbat = AHbat/3600
    soc = (AHbat/50)*100
    print(soc)

def growthRateComparison():
    n     = []
    sqrtP = []
    logP  = []
    nlogP = []
    nSqP  = []
    nCubP = []
    n2P   = []
    n3P   = []
    nnP   = []
    for i in range(1,6):
        n.append(i)
        #sqrtP.append('{:.2f}'.format(math.sqrt(i)))
        sqrtP.append(math.sqrt(i))
        logP.append(math.log2(i))
        nlogP.append(i*(math.log2(i)))
        nSqP.append(i**2)
        nCubP.append(i**3)
        n2P.append(2**i)
        n3P.append(3**i)
        nnP.append(i**i)
        #print('{:.2f}'.format(math.sqrt(i)), '{:.2f}'.format(math.log10(i)))
    plt.plot(n, sqrtP)
    plt.plot(n, logP)
    plt.plot(n, nlogP)
    plt.plot(n, nSqP)
    plt.plot(n, nCubP)
    plt.plot(n, n2P)
    plt.plot(n, n3P)
    plt.plot(n, nnP)
    plt.grid()
    plt.show()


#twon_one(50)
#testCollatzConj(1000)
#calcPi()
#print("max size = ", sys.maxsize)
#print(fibonacci(3000000))
#summation()
growthRateComparison()

