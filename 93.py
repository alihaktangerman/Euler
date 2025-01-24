from collections import deque
from itertools import permutations, combinations, count

template = deque()
templates = []

def solve():
    templatestring = "".join(template)
    if templatestring.count("_") == 4:
        templates.append(list(templatestring))
    elif len(template) == 0:
        template.append("(_+_)")
        solve()
        template.pop()
        template.append("(_-_)")
        solve()
        template.pop()
        template.append("(_*_)")
        solve()
        template.pop()
        template.append("(_/_)")
        solve()
        template.pop()
    else:
        template.appendleft("(_+")
        template.append(")")
        solve()
        template.popleft()
        template.pop()
        template.appendleft("(_-")
        template.append(")")
        solve()
        template.popleft()
        template.pop()
        template.appendleft("(_*")
        template.append(")")
        solve()
        template.popleft()
        template.pop()
        template.appendleft("(_/")
        template.append(")")
        solve()
        template.popleft()
        template.pop()
        template.appendleft("(")
        template.append("+_)")
        solve()
        template.popleft()
        template.pop()
        template.appendleft("(")
        template.append("-_)")
        solve()
        template.popleft()
        template.pop()
        template.appendleft("(")
        template.append("*_)")
        solve()
        template.popleft()
        template.pop()
        template.appendleft("(")
        template.append("/_)")
        solve()
        template.popleft()
        template.pop()
        
solve()

def solve2(nums):
    solutions = set()
    for perm in permutations(nums):
        for template in templates:
            template = [_ for _ in template]
            counter = 0
            for i in range(len(template)):
                if template[i] == "_":
                    template[i] = str(perm[counter])
                    counter += 1
            try:
                expression = "".join(template)

                x = eval(expression)
                if x > 0 and abs(round(x)-x) < 1e-4:
                    solutions.add(round(x))
            except:
                pass
    length = 0
    for i in count(1):
        if i in solutions:
            length += 1
        else:
            return length
    
print(solve2([1,2,3,4]))

best = [1,2,3,4]
max = 28

for nums in combinations(list(range(1,10)),4):
    print(nums)
    if solve2(nums) > max:
        max = solve2(nums)
        best = nums
        
print(best)
