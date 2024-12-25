import sympy

limit = 100000

radicals = [1 for i in range(limit+1)]

primes = list(sympy.primerange(2, limit+1))

for prime in primes:
    for i in range(prime, limit+1, prime):
        radicals[i] *= prime

print(sorted(range(len(radicals)), key=lambda x: radicals[x])[10000])
