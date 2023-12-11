import itertools

with open('input.txt') as f:
    data = f.read()


grid = [[ch for ch in line] for line in data.splitlines()]

empty_i = []
for i, line in enumerate(grid):
    if all(ch == '.' for ch in line):
        empty_i.append(i)

empty_j = []
for j, col in enumerate(zip(*grid)):
    if all(ch == '.' for ch in col):
        empty_j.append(j)

galaxies = []
for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if ch == '#':
            galaxies.append((i, j))


ans1 = 0
ans2 = 0
for g1, g2 in itertools.combinations(galaxies, 2):
    i, j, ii, jj = *g1, *g2

    d1 = 0
    d2 = 0
    for iii in empty_i:
        if i < iii < ii or i > iii > ii:
            d1 += 1
            d2 += 1000000-1
    for jjj in empty_j:
        if j < jjj < jj or j > jjj > jj:
            d1 += 1
            d2 += 1000000-1

    ans1 += abs(i-ii) + abs(j-jj) + d1
    ans2 += abs(i-ii) + abs(j-jj) + d2
    
print("Part 1:", ans1)
print("Part 2:", ans2)
