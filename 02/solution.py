import math

with open('input.txt') as f:
    data = f.read()


inventory = {
    'red': 12,
    'green': 13,
    'blue': 14
}

res1 = res2 = 0

for line in data.splitlines():

    game, rem = line.split(': ')
    game = int(game.split()[-1])

    sets = rem.split('; ')

    requirements = {'red':0, 'green':0, 'blue':0}

    for s in sets:
        colors = s.split(', ')
        for color in colors:
            n, c = color.split()
            n = int(n)
            requirements[c] = max(requirements[c], n)

    if all(requirements[k] <= inventory[k] for k in requirements.keys()):
        res1 += game

    res2 += math.prod(requirements.values())


print("Part 1:", res1)
print("Part 2:", res2)
