import math

with open('input.txt') as f:
    data = f.read()


def get_overlap(line):
    winning_nums, my_nums = line.split(': ')[1].split(' | ')
    winning_nums = set(map(int, winning_nums.split()))
    my_nums = set(map(int, my_nums.split()))
    return len(set.intersection(winning_nums, my_nums))


cards = [get_overlap(line) for line in data.splitlines()]
won_cards = [1] * len(cards)


points = 0

for i, overlap in enumerate(cards):
    points += math.floor(2 ** (overlap - 1))

    for ii in range(overlap):
        won_cards[i + ii + 1] += won_cards[i]


print("Part 1:", points)
print("Part 2:", sum(won_cards))
