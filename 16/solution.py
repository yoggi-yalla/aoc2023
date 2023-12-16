with open('input.txt') as f:
    data = f.read()

dirs = (
    (0,1),
    (1,0),
    (0,-1),
    (-1,0),
)

grid = [[ch for ch in line] for line in data.splitlines()]


def in_grid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


def next_beams(beams):
    next_beams = set()
    for i, j, d in beams:
        di, dj = dirs[d]
        ii, jj = i+di, j+dj
        if in_grid(ii, jj):
            if grid[ii][jj] == '.':
                next_beams.add((ii, jj, d))
            elif grid[ii][jj] == '\\':
                if d == 0:
                    next_beams.add((ii, jj, 1))
                elif d == 1:
                    next_beams.add((ii, jj, 0))
                elif d == 2:
                    next_beams.add((ii, jj, 3))
                elif d == 3:
                    next_beams.add((ii, jj, 2))
                else:
                    raise Exception
            elif grid[ii][jj] == '/':
                if d == 0:
                    next_beams.add((ii, jj, 3))
                elif d == 3:
                    next_beams.add((ii, jj, 0))
                elif d == 1:
                    next_beams.add((ii, jj, 2))
                elif d == 2:
                    next_beams.add((ii, jj, 1))
                else:
                    raise Exception
            elif grid[ii][jj] == '-':
                if d in (0, 2):
                    next_beams.add((ii, jj, d))
                else:
                    next_beams.add((ii, jj, 0))
                    next_beams.add((ii, jj, 2))
            elif grid[ii][jj] == '|':
                if d in (1, 3):
                    next_beams.add((ii, jj, d))
                else:
                    next_beams.add((ii, jj, 1))
                    next_beams.add((ii, jj, 3))
            else:
                raise Exception

    return next_beams


def run(beam):

    beams = set([beam])

    state = frozenset(beams)
    states = set()

    energized = set()

    while state not in states:
        states.add(state)

        for i, j, _ in beams:
            if in_grid(i, j):
                energized.add((i, j))

        beams = next_beams(beams)
        state = frozenset(beams)

    return len(energized)


def part_2():
    best_ans = 0
    for i in range(len(grid)):
        best_ans = max(best_ans, run((i, -1, 0)))
        best_ans = max(best_ans, run((i, len(grid[i]), 2)))
    for j in range(len(grid[0])):
        best_ans = max(best_ans, run((-1, j, 1)))
        best_ans = max(best_ans, run((len(grid), j, 3)))
    return best_ans


print("Part 1:", run((0,-1,0)))
print("Part 2:", part_2())
