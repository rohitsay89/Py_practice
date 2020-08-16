# This file is for simple math calculation scripts
step_count = 0


# (2^n -1) printing values upto n = 10
def twon_one():
    for i in range(0, 100):
        y = (pow(2, i) - 1)
        print(y)

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


def testCollatzConj(n):
    for i in range(1, n):
        print(i, threen_plus_one(i))

#twon_one()
testCollatzConj(1000)