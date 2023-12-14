with open('input.txt') as f:
    data = f.read()


grid1 = [[ch for ch in line] for line in data.splitlines()]
grid2 = [[ch for ch in line] for line in data.splitlines()]


boulder_positions1 = []
for i, line in enumerate(grid1):
    for j, ch in enumerate(line):
        if ch == 'O':
            boulder_positions1.append((i, j))
boulder_positions2 = boulder_positions1.copy()


directions1 = ((-1,0),)
directions2 = ((-1,0), (0,-1), (1,0), (0,1),)


def in_grid(i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


def to_string(grid):
    return "".join(["".join(line) for line in grid])


def run_cycle(grid, directions, boulder_positions):
    for di, dj in directions:
        while True:
            unchanged = True
            for p, (i, j) in enumerate(boulder_positions):
                ii, jj = i+di, j+dj
                while in_grid(ii, jj, grid) and grid[ii][jj] == '.':
                    iii, jjj = ii+di, jj+dj
                    if in_grid(iii, jjj, grid) and grid[iii][jjj] == '.':
                        ii, jj = iii, jjj
                        continue
                    unchanged = False
                    boulder_positions[p] = (ii, jj)
                    grid[i][j] = '.'
                    grid[ii][jj] = 'O'

            if unchanged:
                break

    return boulder_positions


def count(grid):
    ans = 0
    for i, line in enumerate(grid):
        c = "".join(line).count('O')
        ans += c * (len(grid) - i)
    return ans


def part_1():
    run_cycle(grid1, directions1, boulder_positions1)
    return count(grid1)


def part_2():
    seen = set()
    history = []
    bp = boulder_positions2

    s = to_string(grid2)

    i = 0
    while s not in seen:
        seen.add(s)
        history.append(s)
        bp = run_cycle(grid2, directions2, bp)
        s = to_string(grid2)
        i += 1

    cycle_start = history.index(s)
    cycle_end = i
    cycle_length = cycle_end - cycle_start

    m = (1000000000 - cycle_start) % cycle_length

    for _ in range(m):
        bp = run_cycle(grid2, directions2, bp)

    return count(grid2)


print("Part 1:", part_1())
print("Part 2:", part_2())
