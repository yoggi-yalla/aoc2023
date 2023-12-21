with open('input.txt') as f:
    data = f.read()


grid = [[ch for ch in line] for line in data.splitlines()]


for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if ch == 'S':
            grid[i][j] = '.'
            start = i, j
            break


dirs = (
    (1,0),
    (0,1),
    (-1,0),
    (0,-1),
)


def in_grid(i, j):
    return 0 <= i < len(grid) and 0 <= j <len(grid[i])


def neighbors(i, j):
    for di, dj in dirs:
        ii, jj = i+di, j+dj
        if in_grid(ii, jj):
            yield ii, jj


def count(start, steps):

    prev = set()
    prevprev = set()
    current = set([start])

    def get_next(current, prev, prevprev):
        frontier = current - prevprev

        next = set()
        for i, j in frontier:
            for ii, jj in neighbors(i, j):
                if grid[ii%len(grid)][jj%len(grid[0])] == '.':
                    next.add((ii, jj))
        
        return set.union(next, prev), current, prev

    for _ in range(steps):
        current, prev, prevprev = get_next(current, prev, prevprev)
    
    return len(current)

print("Part 1:", count(start, 64))


N_EVEN = count(start, 132)
N_ODD = count(start, 131)

K = 26501365//131

ans = 0
ans += (K * K) * N_EVEN
ans += (K - 1) * (K - 1) * N_ODD

ans += count((0,65),130)
ans += count((130,65),130)
ans += count((65,0),130)
ans += count((65,130),130)

ans += (K-1) * count((0,0),195)
ans += (K-1) * count((0,130),195)
ans += (K-1) * count((130,0),195)
ans += (K-1) * count((130,130),195)

ans += K * count((0,0),64)
ans += K * count((0,130),64)
ans += K * count((130,0),64)
ans += K * count((130,130),64)

print("Part 2:", ans)
