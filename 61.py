from itertools import count

triangles = []
squares = []
pentagonals = []
hexagonals = []
heptagonals = []
octagonals = []

def triangle(n): return n*(n+1)//2
def square(n): return n*n
def pentagonal(n): return n*(3*n-1)//2
def hexagonal(n): return n*(2*n-1)
def heptagonal(n): return n*(5*n-3)//2
def octagonal(n): return n*(3*n-2)

for i in count(1):
    t = triangle(i)
    s = square(i)
    p = pentagonal(i)
    h = hexagonal(i)
    hp = heptagonal(i)
    o = octagonal(i)
    
    if 999 < t < 10000: triangles.append(t)
    if 999 < s < 10000: squares.append(s)
    if 999 < p < 10000: pentagonals.append(p)
    if 999 < h < 10000: hexagonals.append(h)
    if 999 < hp < 10000: heptagonals.append(hp)
    if 999 < o < 10000: octagonals.append(o)
    
    if t >= 10000 and s >= 10000 and p >= 10000 and h >= 10000 and hp >= 10000 and o >= 10000:
        break

all = [triangles, squares, pentagonals, hexagonals, heptagonals, octagonals]    

used = [False for i in range(6)]
numbers = []

def solve():
    if len(numbers) == 6 and numbers[0] // 100 == numbers[-1] % 100:
        print(numbers)
        print(sum(numbers))
        return
    for i in range(6):
        if not used[i]:
            for j in all[i]:
                if len(numbers) == 0 or str(numbers[-1])[-2:] == str(j)[:2]:
                    numbers.append(j)
                    used[i] = True
                    solve()
                    numbers.pop()
                    used[i] = False
                    
solve()
