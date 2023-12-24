from z3 import Int, Solver
import itertools

with open('input.txt') as f:
    data = f.read()

def parse_line(line):
    line = line.replace(' @', ',')
    return tuple(map(int, line.split(', ')))

crystals = [parse_line(line) for line in data.splitlines()]

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

lines = []
for x, y, z, dx, dy, dz in crystals:
    xx, yy, zz = x+dx, y+dy, z+dz
    lines.append((line((x, y), (xx, yy)), x, y, z, dx, dy, dz))


test_area = (200000000000000, 400000000000000)

ans1 = 0
for l1, l2 in itertools.combinations(lines, 2):

    l1, x1, y1, z1, dx1, dy1, dz1 = l1
    l2, x2, y2, z2, dx2, dy2, dz2 = l2

    cross = intersection(l1, l2)

    if cross:
        x, y = cross
        t1 = (x-x1) / dx1
        t2 = (x-x2) / dx2

        if test_area[0] <= x <= test_area[1] and test_area[0] <= y <= test_area[1] and t1 >= 0 and t2 >= 0:
            ans1 += 1

print("Part 1:", ans1)


s = Solver()

x = Int('x')
y = Int('y')
z = Int('z')
dx = Int('dx')
dy = Int('dy')
dz = Int('dz')

constraints = []

for i, c in enumerate(crystals):
    xx, yy, zz, dxx, dyy, dzz = c

    t = Int(f't_{i}')
    s.add(t > 0)

    s.add(x == xx + (dxx - dx) * t)
    s.add(y == yy + (dyy - dy) * t)
    s.add(z == zz + (dzz - dz) * t)


s.check()
ans2 = s.model()[x].as_long() + s.model()[y].as_long() + s.model()[z].as_long()

print("Part 2:", ans2)
