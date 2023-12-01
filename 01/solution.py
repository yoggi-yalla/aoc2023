with open('input.txt') as f:
    data = f.read()

import re

pattern1 = r'\d'
pattern2 = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'


string_to_digit = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}

tot1 = 0
tot2 = 0


for line in data.splitlines():
    nums1 = re.findall(pattern1, line)
    nums2 = re.findall(pattern2, line)
    nums2 = [string_to_digit.get(n, n) for n in nums2]

    n1 = int(nums1[0] + nums1[-1])
    n2 = int(nums2[0] + nums2[-1])

    tot1 += n1
    tot2 += n2


print("Part 1:", tot1)
print("Part 2:", tot2)
