with open('dummyinput.txt') as f:
    data = f.read()

'''
data = """
#S#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################E#
""".strip()
'''


grid = [[ch for ch in line] for line in data.splitlines()]

juncs = []

for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if ch in '<>^v':
            juncs.append((i,j))


start = (0,1)
goal = (len(grid)-1, len(grid[0])-2)


juncs.insert(0,start)
juncs.append(goal)


dirs = (
    (1,0),
    (0,1),
    (-1,0),
    (0,-1),
)

def in_grid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


def neighbors(i, j):
    for di, dj in dirs:
        ii, jj = i+di, j+dj
        if in_grid(ii, jj):
            yield (ii, jj)


from collections import deque



def path_between_juncs(j1, j2):
    start_state = (*j1, frozenset())

    q = deque()
    q.append(start_state)

    while q:
        i, j, path = q.popleft()

        if (i, j) == j2:
            return len(path)-1, path - frozenset([j1])

        if (i, j) in path:
            continue

        if len(path) > 0 and grid[i][j] in '^<>v':
            continue

        for ii, jj in neighbors(i, j):
            if grid[ii][jj] != '#':
                q.append((ii, jj, path.union(frozenset([(i,j)]))))
    
    return 0, tuple()


from collections import defaultdict
juncmap = defaultdict(list)
juncmap2 = {}
juncmap3 = {}

import itertools

for (i,j), (ii,jj) in itertools.combinations(juncs, 2):
    l, path = path_between_juncs((i,j),(ii,jj))
    if l > 0:
        juncmap[i,j].append((ii,jj,l))
        juncmap[ii,jj].append((i,j,l))

        juncmap2[i,j,ii,jj] = (l)
        juncmap2[ii,jj,i,j] = (l)

        juncmap3[i,j,ii,jj] = path
        juncmap3[ii,jj,i,j] = path




q = deque()

start_state = (*start, tuple())

q.append(start_state)

solutions = []

while q:
    i, j, path = q.popleft()

    if (i, j) in path:
        continue

    for ii, jj, l in juncmap[i,j]:
        q.append((ii, jj, path + ((i,j),)))

    if (i, j) == goal:
        solutions.append(path+((i,j),))


new_sols = []
for s in solutions:
    new_sols.append((sum(juncmap2[i,j,ii,jj] for (i,j),(ii,jj) in zip(s,s[1:]))+len(s)-1,s))

new_sols.sort(reverse=True)
solutions=new_sols


def valid_path(path):
    seen = set()

    for (i,j),(ii,jj) in zip(path, path[1:]):
        fullset = set([*juncmap3[i,j,ii,jj]])

        if len(seen.intersection(fullset)) > 0:
            return False
        
        seen = seen.union(fullset)
    
    return True


for l, path in solutions[:1000]:
    if valid_path(path):
        print(l)
        print(path)
        break
