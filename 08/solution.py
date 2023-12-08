import math
from itertools import cycle

with open('input.txt') as f:
    data = f.read()


instruction, maps = data.split('\n\n')

m = {}
for line in maps.splitlines():
    start, rem = line.split(' = ')
    rem = rem.replace('(', '').replace(')', '')
    left, right = rem.split(', ')
    m[start] = (left, right)


def solve_1(pos='AAA', part_2=False):
    steps = 0
    c = cycle(instruction)
    while True:
        if not part_2 and pos == 'ZZZ':
            return steps

        if part_2 and pos[-1] == 'Z':
            return steps

        cc = next(c)
        
        if cc == 'R':
            pos = m[pos][1]
        else:
            pos = m[pos][0]
        
        steps += 1


def solve_2():
    positions = [k for k in m if k[-1] == 'A']

    steps = [solve_1(p, True) for p in positions]

    return math.lcm(*steps)


print("Part 1:", solve_1())
print("Part 2:", solve_2())
