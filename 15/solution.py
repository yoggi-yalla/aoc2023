from collections import defaultdict
import re

with open('input.txt') as f:
    data = f.read()


def hash(x):
    s = 0
    for ch in x:
        s += ord(ch)
        s *= 17
        s %= 256
    return s


m = defaultdict(list)

ans1 = 0
for line in data.split(','):
    ans1 += hash(line)

    h, v = re.split(r'-|=', line)
    box_nbr = hash(h)

    if v:
        for i, e in enumerate(m[box_nbr]):
            if e[0] == h:
                m[box_nbr][i] = (h, int(v))
                break
        else:
            m[box_nbr].append((h, int(v)))
    else:
        for i, e in enumerate(m[box_nbr]):
            if e[0] == h:
                m[box_nbr].pop(i)
    

ans2 = 0
for k, v in m.items():
    for i, lens in enumerate(v):
        ans2 += (k+1) * (i+1) * lens[1]


print("Part 1:", ans1)
print("Part 2:", ans2)
