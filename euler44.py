from math import isqrt

def ispentagonal(x):
    n = isqrt(2*x//3) + 1
    return pentagonal(n) == x

def pentagonal(n):
    return n*(3*n-1)//2

for i in range(1,10000):
    for j in range(i+1,10000):
        x = pentagonal(i)
        y = pentagonal(j)
        if ispentagonal(y+x) and ispentagonal(y-x):
            print(x,y,y-x)
