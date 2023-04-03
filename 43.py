from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]
used = [False]*10
start_from = list(filter(lambda p: p[0] != 0, map(list, permutations(list(range(10)), 3))))
div_rule = {2: (0, 0, 1), 3: (1, 1, 1), 5: (0, 0, 1), 7: (2, 3, 1), 11: (1, 10, 1), 13: (9, 10, 1), 17: (15, 10, 1)}

perm = [1, 4, 0]
for p in perm: used[p] = True
ans = 0


def find(n):
    global perm, ans, used
    if n == 10:
        print(int("".join(map(str, perm))))
        ans += int("".join(map(str, perm)))
    for x in range(10):
        if not used[x]:
            rule = div_rule[primes[n-3]]
            perm.append(x)
            used[x] = True
            if (perm[-3]*rule[0] + perm[-2]*rule[1] + perm[-1]*rule[2]) % primes[n-3] == 0:
                find(n+1)
            perm.pop()
            used[x] = False


def run():
    global perm, used
    for start in start_from:
        for x in start:
            used[x] = True
        perm = start
        find(3)
        used = [False] * 10


run()
print(f"ans={ans}")

