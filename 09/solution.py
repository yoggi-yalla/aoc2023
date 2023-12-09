with open('input.txt') as f:
    data = f.read()


ans1 = ans2 = 0

for line in data.splitlines():

    nums = list(map(int, line.split()))
    all_nums = [nums]

    while not all(n == 0 for n in nums):
        new_nums = []
        for n, nn, in zip(nums, nums[1:]):
            new_nums.append(nn-n)
        all_nums.append(new_nums)
        nums = new_nums


    all_nums[-1].extend([0,0])

    for i in range(len(all_nums)-2, -1, -1):
        all_nums[i].insert(0, all_nums[i][0] - all_nums[i+1][0])
        all_nums[i].append(all_nums[i][-1] + all_nums[i+1][-1])

    ans1 += all_nums[0][-1]
    ans2 += all_nums[0][0]
    

print("Part 1:", ans1)
print("Part 2:", ans2)
