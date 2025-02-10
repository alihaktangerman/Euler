from itertools import permutations
from sympy import isprime

visited = {i:False for i in range(1,10)}
primes = []

counter = 0

def solve():
    global counter
    if sorted(primes) != primes:
        return
    if not any(not visited[i] for i in range(1,10)):
        counter += 1
        return
    usable = [i for i in range(1,10) if not visited[i]]
    canididates = [int("".join(map(str,perm))) for i in range(1,len(usable)+1) for perm in permutations(usable,i)]
    for canididate in canididates:
        if isprime(canididate):
            primes.append(canididate)
            for digit in str(canididate):
                visited[int(digit)] = True
            solve()
            for digit in str(canididate):
                visited[int(digit)] = False
            primes.pop()
    print(counter)
solve()
