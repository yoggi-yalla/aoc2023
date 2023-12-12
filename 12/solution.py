import functools

with open('input.txt') as f:
    data = f.read()


@functools.cache
def valid_ways(springs, groups):
    if len(groups) == 0:
        if '#' not in springs:
            return 1
        else:
            return 0

    group = groups[0]
    variations = []
    found_hash = False
    for i in range(len(springs)-group+1):
        if found_hash:
            break

        if '.' not in springs[i:i+group]:
            if i + group < len(springs) and springs[i+group] != '#':
                variations.append(springs[i+group+1:])
            elif i + group == len(springs):
                variations.append('')

        if springs[i] == '#':
            found_hash = True

    return sum(valid_ways(s, groups[1:]) for s in variations)


ans1 = ans2 = 0

for line in data.splitlines():
    springs, groups = line.split()

    springs2 = "?".join([springs]*5)
    groups2 = ",".join([groups]*5)

    groups = tuple(map(int, groups.split(',')))
    groups2 = tuple(map(int, groups2.split(',')))

    ans1 += valid_ways(springs, groups)
    ans2 += valid_ways(springs2, groups2)


print("Part 1:", ans1)
print("Part 2:", ans2)
