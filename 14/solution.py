from collections import deque

with open('input.txt') as f:
    data = f.read()


grid1 = [[ch for ch in line] for line in data.splitlines()]
grid2 = [[ch for ch in line] for line in data.splitlines()]


directions1 = ((-1,0),)
directions2 = ((-1,0), (0,-1), (1,0), (0,1),)


def in_grid(i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


def to_string(grid):
    return "".join(["".join(line) for line in grid])


def run_cycle(grid, directions):
    boulder_positions = []
    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if ch == 'O':
                boulder_positions.append((i, j))


    for di, dj in directions:
        while True:
            unchanged = True
            for p, (i, j) in enumerate(boulder_positions):
                ii, jj = i+di, j+dj
                if in_grid(ii, jj, grid) and grid[ii][jj] == '.':
                    unchanged = False
                    boulder_positions[p] = (ii, jj)
                    grid[i][j] = '.'
                    grid[ii][jj] = 'O'

            if unchanged:
                break


def count(grid):
    ans = 0
    for i, line in enumerate(grid):
        c = "".join(line).count('O')
        ans += c * (len(grid)-i)
    return ans


def part_1(grid, directions):
    run_cycle(grid, directions)
    return count(grid)


def part_2(grid, directions):
    seen = set()
    history = []
    
    s = to_string(grid)

    i = 0
    while s not in seen:
        seen.add(s)
        history.append(s)
        run_cycle(grid, directions)
        s = to_string(grid)
        i += 1
    
    cycle_start = history.index(s)
    cycle_end = i
    cycle_length = cycle_end - cycle_start

    m = (1000000000 - cycle_start) % cycle_length

    new_grid = [[ch for ch in line] for line in data.splitlines()]

    for _ in range(cycle_start + m):
        run_cycle(new_grid, directions)
    
    return count(new_grid)


print("Part 1:", part_1(grid1, directions1))
print("Part 2:", part_2(grid2, directions2))
