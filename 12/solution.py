import functools

with open('input.txt') as f:
    data = f.read()


@functools.cache
def valid_ways(springs, groups):
    if not groups:
        if '#' not in springs:
            return 1
        return 0

    group = groups[0]
    remainders = []
    for i in range(len(springs) - group + 1):
        if '.' not in springs[i:i+group]:
            if i + group == len(springs) or springs[i+group] != '#':
                remainders.append(springs[i+group+1:])

        if springs[i] == '#':
            break

    return sum(valid_ways(s, groups[1:]) for s in remainders)


ans1 = ans2 = 0

for line in data.splitlines():
    springs, groups = line.split()
    groups = tuple(map(int, groups.split(',')))

    springs2 = "?".join([springs]*5)
    groups2 = groups*5

    ans1 += valid_ways(springs, groups)
    ans2 += valid_ways(springs2, groups2)


print("Part 1:", ans1)
print("Part 2:", ans2)
