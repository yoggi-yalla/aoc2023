with open('input.txt') as f:
    data = f.read()


'''
data = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
'''

start = (0,0)
pos = start


filled = set()

dirs = {
    'U': (-1,0),
    'D': (1,0),
    'L': (0,-1),
    'R': (0,1),
}

vertices = set()

for line in data.splitlines():
    a, b, c = line.split()

    steps = int(b)
    di, dj = dirs[a]

    for _ in range(steps):
        i, j = pos
        ii, jj = i+di, j+dj
        pos = ii, jj
        filled.add(pos)
    vertices.add((i, j))



max_i = max(x[0] for x in filled)
min_i = min(x[0] for x in filled)

max_j = max(x[1] for x in filled)
min_j = min(x[1] for x in filled)



H = max_i - min_i + 1
W = max_j - min_j + 1

translated = set()

for i, j in filled:
    translated.add((i-min_i, j-min_j))



grid = [['.' for _ in range(W)] for _ in range(H)]


for i, j in translated:
    grid[i][j] = '*'


mid_i, mid_j = H//2, W//2

Q = [(mid_i, mid_j)]


def in_grid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


while Q:
    i, j = Q.pop()

    for di, dj in dirs.values():
        ii, jj = i+di, j+dj
        if in_grid(ii, jj) and grid[ii][jj] == '.':
            Q.append((ii, jj))
            grid[ii][jj] = '@'



for line in grid:
    print("".join(line))


ans = 0
for line in grid:
    s = "".join(line)
    ans += s.count('*') + s.count('@')

print(ans)



