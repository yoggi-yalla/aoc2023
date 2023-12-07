from collections import Counter

with open('input.txt') as f:
    data = f.read()


card_order_1 = "AKQJT98765432" 
card_order_2 = "AKQT98765432J"

hand_types = (
    (5,),
    (4,1),
    (3,2),
    (3,1,1),
    (2,2,1),
    (2,1,1,1),
    (1,1,1,1,1),
)


def get_type_1(hand):
    return hand_types.index(tuple(sorted(Counter(hand).values(), reverse=True)))


def get_type_2(hand):
    return min(get_type_1(hand.replace("J", c)) for c in "23456789TQKA")


def total_winnings(get_type, card_order):
    hands = []
    for line in data.splitlines():
        hand, bet = line.split()
        hand_type = get_type(hand)
        ordered_hand = tuple((card_order.index(c) for c in hand))
        hands.append((hand_type, ordered_hand, hand, int(bet)))
    hands.sort(reverse=True)

    return sum((i + 1) * h[3] for i, h in enumerate(hands))


print("Part 1:", total_winnings(get_type_1, card_order_1))
print("Part 2:", total_winnings(get_type_2, card_order_2))
