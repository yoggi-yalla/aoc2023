import numpy as np

with open('input.txt') as f:
    data = f.read()


def shoelace(x_y):
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)

    return area


dirs1 = {
    'U': (-1,0),
    'D': (1,0),
    'L': (0,-1),
    'R': (0,1),
}


dirs2 = (
    (0,1),   
    (1,0),
    (0,-1),
    (-1,0),
)


pos1 = pos2 = (0,0)

vertices1 = []
vertices2 = []
for line in data.splitlines():
    a, b, c = line.split()
    c = c.replace('(', '').replace(')', '').replace('#', 'x')

    n1 = int(b)
    n2 = int('0'+c[:-1], 16)

    di1, dj1 = dirs1[a]
    di2, dj2 = dirs2[int(c[-1])]

    i1, j1 = pos1
    i2, j2 = pos2

    ii1, jj1 = i1+di1*n1, j1+dj1*n1
    ii2, jj2 = i2+di2*n2, j2+dj2*n2

    i1, j1 = ii1, jj1
    i2, j2 = ii2, jj2

    pos1 = i1, j1
    pos2 = i2, j2

    vertices1.append(pos1)
    vertices2.append(pos2)


def dist(v1, v2):
    i, j, ii, jj = *v1, *v2
    return abs(i-ii) + abs(j-jj)


def area(vertices):
    perimeter = 0
    for v1, v2 in zip(vertices, vertices[1:]):
        perimeter += dist(v1, v2)
    perimeter += dist(vertices[0], vertices[-1])
    return int(shoelace(vertices) + perimeter / 2 + 1)


print("Part 1:", area(vertices1))
print("Part 2:", area(vertices2))
