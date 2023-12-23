import itertools
from collections import defaultdict

with open('input.txt') as f:
    data = f.read()


grid = [[ch for ch in line] for line in data.splitlines()]


dirs = (
    (1,0),
    (0,1),
    (-1,0),
    (0,-1),
)


def in_grid(i,j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


def neighbors(i, j):
    n = []
    for di, dj in dirs:
        ii, jj = i+di, j+dj
        if in_grid(ii, jj) and grid[ii][jj] != '#':
            n.append((ii,jj))
    return n


junctions = set()
for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if ch != '#':
            if len(neighbors(i,j)) > 2:
                junctions.add((i, j))


start = (0, 1)
goal = (len(grid)-1, len(grid[0])-2)

junctions.add(start)
junctions.add(goal)


def path_between(j1, j2, part):
    
    q = [(*j1, tuple(), frozenset())]

    while q:
        i, j, path, pathset = q.pop()

        if (i, j) == j2:
            return path
        
        if (i, j) in pathset:
            continue
        
        if len(path) > 0 and (i, j) in junctions:
            continue

        if part == 1 and grid[i][j] in '<>^v':
            if grid[i][j] == '<': q.append((i,j-1,path+((i,j),),pathset.union(frozenset([(i,j)]))))
            if grid[i][j] == '>': q.append((i,j+1,path+((i,j),),pathset.union(frozenset([(i,j)]))))
            if grid[i][j] == '^': q.append((i-1,j,path+((i,j),),pathset.union(frozenset([(i,j)]))))
            if grid[i][j] == 'v': q.append((i+1,j,path+((i,j),),pathset.union(frozenset([(i,j)]))))
            continue

        for ii,jj in neighbors(i, j):
            q.append((ii, jj, path+((i,j),),pathset.union(frozenset([(i,j)]))))


def paths_to_target(j_map):
    paths = set()

    q = [(0, 1, tuple(), frozenset())]

    while q:
        i, j, path, pathset = q.pop()

        if (i, j) == goal:
            paths.add(path+((i,j),))

        if (i, j) in pathset:
            continue
        
        for ii, jj in j_map[i,j]:
            q.append((ii, jj, path + ((i,j),), pathset.union(frozenset([(i,j)]))))
    
    return paths


def solve(part):
    j_paths = {}
    j_map = defaultdict(list)
    for j1, j2 in itertools.product(junctions, junctions):
        if j1 == j2:
            continue
        path = path_between(j1, j2, part)
        if path:
            j_paths[j1, j2] = path
            j_map[j1].append(j2)

    ans = 0
    for p in paths_to_target(j_map):
        ans = max(ans, sum(len(j_paths[j1,j2]) for j1, j2 in zip(p, p[1:])))

    return ans


print("Part 1:", solve(1))
print("Part 2:", solve(2))
