import heapq
import itertools
import functools
import collections


with open('input.txt') as f:
    data = f.read()



line = ".??..??...?##. 1,1,3"

line = "???.### 1,1,3"
line = "?###???????? 3,2,1"

valid_ways = 0

for line in data.splitlines():
    springs, groups = line.split()
    groups = list(map(int, groups.split(',')))

    for c in itertools.combinations(list(range(len(springs))), len(groups)):
        l = list(springs)
        broken = False
        for i, place in enumerate(c):
            for j in range(groups[i]):
                if place + j < len(l) and l[place+j] in ('?', '#'):
                    l[place+j] = '@'
                    continue
                else:
                    broken = True
                    break
            if broken:
                break
    

        if not broken:
            x = "".join(l)
            x = x.replace('#', '@')
            import re
            y = (list(map(len, re.findall(r'@+', x))))
            if y == groups:
                valid_ways += 1





print(valid_ways)



