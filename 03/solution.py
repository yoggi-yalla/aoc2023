with open('input.txt') as f:
    data = f.read()


grid = [[ch for ch in line] for line in data.splitlines()]


symbols = []
gears = []
starts = []
ends = []


for row in range(len(grid)):
    for col in range(len(grid[row])):
        if not grid[row][col].isdigit() and grid[row][col] != '.':
            symbols.append((row, col))

        if grid[row][col] == '*':
            gears.append((row, col))

        if grid[row][col].isdigit() and (col==0 or not grid[row][col-1].isdigit()):
            starts.append((row, col))

        if grid[row][col].isdigit() and (col==len(grid[row])-1 or not grid[row][col+1].isdigit()):
            ends.append((row, col))


def get_num(start, end):
    return int("".join(grid[start[0]][start[1]:end[1]+1]))


def is_adjacent(start, end, position):
    return (
        start[0] - 1 <= position[0] <= end[0] + 1 and
        start[1] - 1 <= position[1] <= end[1] + 1
    )


part1 = 0
part2 = 0

for s, e in zip(starts, ends):
    if any(is_adjacent(s, e, p) for p in symbols):
        part1 += get_num(s, e)

for p in gears:
    nums = []
    for s, e in zip(starts, ends):
        if is_adjacent(s, e, p):
            nums.append(get_num(s, e))
    if len(nums) == 2:
        part2 += nums[0] * nums[1]


print("Part 1:", part1)
print("Part 2:", part2)
