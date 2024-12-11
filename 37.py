from sympy import isprime

def istruncatable(p):
    s = str(p)
    n = len(s)
    return all(isprime(int(s[i:])) for i in range(n)) and all(isprime(int(s[:i])) for i in range(1,n))

t = []

for i in range(10,1000000):
    if istruncatable(i):
        t.append(i)
        
print(sum(t))
    
    
