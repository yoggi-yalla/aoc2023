import copy

with open('input.txt') as f:
    data = f.read()


def parse_line(line):
    x, y, z, xx, yy, zz = map(int, line.replace('~', ',').split(','))
    return min(x, xx), min(y, yy), min(z, zz), max(x, xx), max(y, yy), max(z, zz)


all_points = set()
bricks = {}

for bricknbr, line in enumerate(data.splitlines()):
    xmi, ymi, zmi, xma, yma, zma = parse_line(line)

    points = set()

    for x in range(xmi, xma+1):
        for y in range(ymi, yma+1):
            for z in range(zmi, zma+1):
                points.add((x, y, z))
                all_points.add((x, y, z))
            
    bricks[bricknbr] = points


while True:
    buffer = []

    for k, v in bricks.items():
        other_points = all_points - v

        for x, y, z in v:
            if (x, y, z-1) in other_points or z == 1:
                break
        else:
            buffer.append(k)

    if not buffer:
        break

    for k in buffer:
        points = bricks[k]
        all_points = all_points - points
        new_points = set()

        for x, y, z in points:
            new_points.add((x, y, z-1))
            all_points.add((x, y, z-1))
        
        bricks[k] = new_points


deps = {k:set() for k in bricks}
for k, v in bricks.items():
    for kk, vv in bricks.items():
        if kk == k:
            continue

        for x, y, z in v:
            if (x, y, z-1) in vv:
                deps[k].add(kk)


def chain_reaction(deps, brick):

    deps = copy.deepcopy(deps)
    
    n = 0
    buffer = [brick]
    while buffer:
        brick = buffer.pop()
        for k, v in deps.items():
            if brick in v:
                deps[k].remove(brick)
                if len(v) == 0:
                    buffer.append(k)
                    n += 1
    return n


ans1 = ans2 = 0
for k in bricks:
    n = chain_reaction(deps, k)

    if n == 0:
        ans1 += 1
    ans2 += n


print("Part 1:", ans1)
print("Part 2:", ans2)
