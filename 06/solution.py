import math

times = [47, 84, 74, 67]
distances = [207, 1394, 1209, 1014]

part1 = 1

for t, d in zip(times, distances):
    start = math.ceil((t - math.sqrt(t**2-4*d)) / 2)
    end = math.floor((t + math.sqrt(t**2-4*d)) / 2)
    part1 *= (end - start + 1)
    

t2 = int("".join(map(str, times)))
d2 = int("".join(map(str, distances)))

start2 = math.ceil((t2 - math.sqrt(t2**2-4*d2)) / 2)
end2 = math.floor((t2 + math.sqrt(t2**2-4*d2)) / 2)

part2 = (end2 - start2 + 1)

print("Part 1:", part1)
print("Part 2:", part2)
