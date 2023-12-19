import math
from collections import defaultdict

with open('input.txt') as f:
    data = f.read()


g1, g2 = data.split('\n\n')


workflows = defaultdict(list)
for line in g1.splitlines():
    a, b = line.split('{')
    b = b[:-1]

    c = b.split(',')

    for rule in c:
        workflows[a].append(rule)


expressions = []

q = [('True', 'in')]

while q:
    expr, pos = q.pop()
    
    if pos == 'R':
        continue
    if pos == 'A':
        expressions.append(expr)
        continue

    for rule in workflows[pos]:
        if ':' not in rule:
            q.append((expr, rule))
        else:
            a, b = rule.split(':')
            q.append((expr + f' and {a}', b))
            if '<' in a:
                a = a.replace('<', '>=')
            else:
                a = a.replace('>', '<=')
            expr = expr + f' and {a}'


ans1 = 0
for line in g2.splitlines():
    line = line[1:-1]
    for ss in line.split(','):
        exec(ss)
    
    if any(eval(exp) for exp in expressions):
        ans1 += x+m+a+s


ans2 = 0
for e in expressions:
    xmin, xmax = 1, 4000
    mmin, mmax = 1, 4000
    amin, amax = 1, 4000
    smin, smax = 1, 4000

    for rule in e.split(' and ')[1:]:
        if '<' in rule:
            if '<=' in rule:
                a, b = rule.split('<=')
                exec(f'{a}max = int(b)')
            else:
                a, b = rule.split('<')
                exec(f'{a}max = int(b)-1')
        elif '>' in rule:
            if '>=' in rule:
                a, b = rule.split('>=')
                exec(f'{a}min = int(b)')
            else:
                a,b = rule.split('>')
                exec(f'{a}min = int(b)+1')

    
    ans2 += math.prod([xmax-xmin+1, mmax-mmin+1, amax-amin+1, smax-smin+1])


print("Part 1:", ans1)
print("Part 2:", ans2)
