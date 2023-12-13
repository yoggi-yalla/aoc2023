with open('input.txt') as f:
    data = f.read()


def count_diff(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)


def count_smudges(l1, l2):
    return sum(count_diff(s1, s2) for s1, s2 in zip(l1, l2))


def find_pivot(l, goal):
    for i in range(1, len(l)):
        j = min(i, len(l) - i)
        s = count_smudges(l[i-j:i], l[i:i+j][::-1])
        if s == goal:
            return i


def transpose(g):
    return [list(col) for col in (zip(*g))]


def summarize(g, goal):
    i = find_pivot(g, goal) or 0
    j = find_pivot(transpose(g), goal) or 0
    return i * 100 + j


ans1 = ans2 = 0
for grid in data.split('\n\n'):
    g = [[ch for ch in line] for line in grid.splitlines()]

    ans1 += summarize(g, 0)
    ans2 += summarize(g, 1)

print("Part 1:", ans1)
print("Part 2:", ans2)
