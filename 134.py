import sympy
from functools import reduce

limit = 1000000

primes = list(sympy.primerange(5, limit))

def chinese_remainder(a, m):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def find_s(p1, p2):
    return chinese_remainder((0, p1), (p2, 10**len(str(p1))))

print(chinese_remainder((0, 19), (23, 100)))

print(find_s(19, 23))

s = 0

for i in range(len(primes)-1):
    print(i)
    s += find_s(primes[i], primes[i+1])

s += find_s(primes[-1], sympy.nextprime(primes[-1]))

print(s)
