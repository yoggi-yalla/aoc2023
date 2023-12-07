from collections import Counter, defaultdict

with open('input.txt') as f:
    data = f.read()


def run(data, nums, part_2=False):
    hands = []

    for line in data.splitlines():
        hand, bet = line.split()
        hand = [nums.index(c) for c in hand]
        bet = int(bet)

        counts = defaultdict(int)

        for i in hand:
            if part_2 and i == 12:
                continue
            counts[i] += 1

        if part_2:
            best = None
            best_value = 0
            for k, v in counts.items():
                if v >= best_value:
                    best_value = v
                    best = k

            for i in hand:
                if i == 12:
                    counts[best] += 1
        

        vals = counts.values()

        if any(i == 5 for i in vals):
            category = 0 # Five of a kind

        elif any(i == 4 for i in vals):
            category = 1 # Four of a kind

        elif any(i == 3 for i in vals):
            if any(i == 2 for i in vals):
                category = 2 # Full house
            else:
                category = 3 # Three of a kind
        
        elif any(i == 2 for i in vals):
            if len(counts) == 3:
                category = 4 # Two pairs
            else:
                category = 5 # One pair

        else:
            category = 6 # High card

        
        hands.append((category, hand, bet))

    hands.sort(reverse=True)

    s = 0
    for i, (category, hand, bet) in enumerate(hands):
        s += (i + 1) * bet
    
    return s


nums1 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
nums2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


print("Part 1:", run(data, nums1, False))
print("Part 1:", run(data, nums2, True))
