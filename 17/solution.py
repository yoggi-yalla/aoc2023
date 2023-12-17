import heapq

with open('input.txt') as f:
    data = f.read()


grid = [[int(ch) for ch in line] for line in data.splitlines()]


def in_grid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


def next_step(cost, i, j, di, dj, consecutive, max_steps, min_steps):
    steps = []

    if consecutive < max_steps:
        if in_grid(i+di, j+dj):
            steps.append((cost + grid[i+di][j+dj], i+di, j+dj, di, dj, consecutive+1))
    
    if consecutive >= min_steps:
        if di != 0:
            if in_grid(i, j+1):
                steps.append((cost+grid[i][j+1], i, j+1, 0, 1, 1))
            if in_grid(i, j-1):
                steps.append((cost+grid[i][j-1], i, j-1, 0, -1, 1))
        
        if dj != 0:
            if in_grid(i+1, j):
                steps.append((cost+grid[i+1][j], i+1, j, 1, 0, 1))
            if in_grid(i-1, j):
                steps.append((cost+grid[i-1][j], i-1, j, -1, 0, 1))
        
    return steps


def run(max_steps, min_steps):
    goal = len(grid) - 1, len(grid[-1]) - 1

    seen = set()
    q = [(0, 0, 0, 0, 1, 0), (0, 0, 0, 1, 0, 0)]

    while True:
        cost, i, j, di, dj, consecutive = heapq.heappop(q)

        if (i, j) == goal and consecutive >= min_steps:
            break

        if (i, j, di, dj, consecutive) in seen:
            continue
        seen.add((i, j, di, dj, consecutive))

        for new_cost, ii, jj, ddi, ddj, new_c in next_step(cost, i, j, di, dj, consecutive, max_steps, min_steps):
            heapq.heappush(q, (new_cost, ii, jj, ddi, ddj, new_c))

    return cost


print("Part 1:", run(3, 0))
print("Part 2:", run(10, 4))
