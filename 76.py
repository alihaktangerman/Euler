from functools import lru_cache

dp = [[-1 for i in range(101)] for j in range(101)]

def solve(n,k):
    if dp[n][k] != -1:
        return dp[n][k]
    if n < k:
        dp[n][k] = 0
    elif n == 0: 
        dp[n][k] = 1
    elif k == n: 
        dp[n][k] = 1
    elif k == 0:
        dp[n][k] = 0
    else:
        dp[n][k] = sum(solve(n-k,l) for l in range(k+1))
    return dp[n][k]

def p(n):
    return sum(solve(n,i) for i in range(n+1))

print(p(100))
