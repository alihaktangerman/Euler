from sympy import isprime

from itertools import combinations, permutations
    
combs = list(combinations(list(range(1,10)),4))
combs = set("".join(sorted(str(i))) for i in range(1000,10000))
permss = [list(permutations(comb)) for comb in combs]


permss = [[int("".join(map(str,perm))) for perm in perms] for perms in permss]
prime_permss = [list(set(filter(lambda x: isprime(x) and x > 999,perms))) for perms in permss]

for perms in prime_permss:
    for i in range(len(perms)):
        for j in range(i+1,len(perms)):
            if perms[j]+perms[j]-perms[i] in perms:
                print(perms)
