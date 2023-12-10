with open('input.txt') as f:
    data = f.read()


grid = [[ch for ch in line] for line in data.splitlines()]

for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if ch == 'S':
            start = (i, j)


connections = {
    '|': [(-1,0),(1,0)],
    '-': [(0,-1),(0,1)],
    'L': [(-1,0),(0,1)],
    'J': [(-1,0),(0,-1)],
    '7': [(0,-1),(1,0)],
    'F': [(1,0),(0,1)],
}


# Manually put the correct value in place of S and take a first step
i, j = start
grid[i][j] = 'J'
prev = start
pos = i - 1, j
steps = 1


main_loop = set([start])

while pos != start:
    main_loop.add(pos)
    i, j = pos
    dirs = connections.get(grid[i][j])

    for di, dj in dirs:
        ii, jj = i + di, j + dj
        if (ii, jj) == prev:
            continue
        else:
            prev = pos
            pos = (ii, jj)
            steps += 1
            break

print("Part 1:", steps//2)


for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if (i, j) not in main_loop:
            grid[i][j] = '.'


inside_points = set()
for i, line in enumerate(grid):
    loop_counter = 0
    for j, ch in enumerate(line):
        if ch == '.' and loop_counter % 2 == 1:
            inside_points.add((i, j))
        if ch in '|LJ':
            loop_counter += 1


print("Part 2:", len(inside_points))
