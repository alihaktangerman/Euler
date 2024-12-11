from functools import lru_cache

@lru_cache
def solve(n):
    if n < 3:
        return 1
    return solve(n-1) + sum(solve(n-k-1) for k in range(3,n)) + 1

print(solve(50))
