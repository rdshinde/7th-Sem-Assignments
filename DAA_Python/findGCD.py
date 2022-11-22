#GCD using recursion

def findGCD(x, y):
    if y == 0:
        return x
    else:
        return findGCD(y, x % y)

#GCD using iteration

def findGCD2(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

