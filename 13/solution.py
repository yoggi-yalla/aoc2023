with open('input.txt') as f:
    data = f.read()


def find_reflection(mirror, invalid_row=0, invalid_col=0):

    rows = ["".join(line) for line in mirror]
    cols = ["".join(col) for col in zip(*mirror)]

    nr = nc = 0

    for i in range(1, len(rows)):
        j = min(i, len(rows)-i)

        if rows[i:i+j] == rows[i-j:i][::-1]:
            if i != invalid_row:
                nr = i
                break

    for i in range(1, len(cols)):
        j = min(i, len(cols)-i)

        if cols[i:i+j] == cols[i-j:i][::-1]:
            if i != invalid_col:
                nc = i
                break
    
    return (nr, nc)


ans1 = ans2 = 0

for g in data.split('\n\n'):
    mirror = [[ch for ch in line] for line in g.splitlines()]

    nr_og, nc_og = find_reflection(mirror)

    found_reflection = False
    for i, line in enumerate(mirror):
        for j, ch in enumerate(line):
            if ch == '#':
                mirror[i][j] = '.'
            else:
                mirror[i][j] = '#'

            nr, nc = find_reflection(mirror, nr_og, nc_og)

            if ch == '#':
                mirror[i][j] = '#'
            else:
                mirror[i][j] = '.'


            if (nr, nc) != (0, 0):
                found_reflection = True
                break

        if found_reflection:
            break

    ans1 += nc_og + 100 * nr_og
    ans2 += nc + 100 * nr


print("Part 1:", ans1)
print("Part 2:", ans2)
