with open('input.txt') as f:
    data = f.read()


grid = [[ch for ch in line] for line in data.splitlines()]


def in_grid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


def run(beam):

    seen = set()
    energized = set()

    q = [beam]

    while q:
        i, j, di, dj = q.pop()

        if (i, j, di, dj) in seen: 
            continue

        seen.add((i, j, di, dj))
        energized.add((i, j))

        ii, jj = i+di, j+dj
        if not in_grid(ii, jj): 
            continue


        match grid[ii][jj]:
            case '/':
                q.append((ii, jj, -dj, -di))
            case '\\':
                q.append((ii, jj, dj, di))
            case '|':
                if dj != 0:
                    q.append((ii, jj, 1, 0))
                    q.append((ii, jj, -1, 0))
                else:
                    q.append((ii, jj, di, dj))
            case '-':
                if di != 0:
                    q.append((ii, jj, 0, 1))
                    q.append((ii, jj, 0, -1))
                else:
                    q.append((ii, jj, di, dj))
            case _:
                q.append((ii, jj, di, dj))

    return len(energized) - 1


def part_2():
    best_ans = 0
    for i in range(len(grid)):
        best_ans = max(best_ans, run((i, -1, 0, 1)))
        best_ans = max(best_ans, run((i, len(grid[i]), 0, -1)))
    for j in range(len(grid[0])):
        best_ans = max(best_ans, run((-1, j, 1, 0)))
        best_ans = max(best_ans, run((len(grid), j, -1, 0)))
    return best_ans


print("Part 1:", run((0, -1, 0, 1)))
print("Part 2:", part_2())
