with open('input.txt') as f:
    data =f.read()


def get_ranges(domain, converter):
    mapppings = []
    domain_min, domain_max = domain

    # find all cases where there is an overlap between converter domains and input domain
    for c in converter:
        src, dest = c
        if domain_min > src[1] or domain_max < src[0]:
            continue

        overlap_start_src = max(domain_min, src[0])
        overlap_end_src = min(domain_max, src[1])
        overlap_start_dest = dest[0] + overlap_start_src - src[0]
        overlap_end_dest = dest[0] + overlap_end_src - src[0]

        mapppings.append(((overlap_start_src, overlap_end_src), (overlap_start_dest, overlap_end_dest)))


    # if no such cases, the entire domain should map to itself
    if not mapppings:
        mapppings.append(((domain_min, domain_max), (domain_min, domain_max)))
    

    # if there are gaps in the domain for the mappings generated above, those gaps must be filled with mappings to itself
    gap_mappings = []


    # if the smallest domain value generated above is greater than domain_min we must fill that gap
    if mapppings[0][0][0] > domain_min:
        gap_mappings.append(((domain_min, mapppings[0][0][0]-1),(domain_min, mapppings[0][0][0]-1)))
    

    # likewise, if the largest domain value generated above is smaller than domain_max we must fill that gap
    if mapppings[-1][0][1] < domain_max:
        gap_mappings.append(((mapppings[-1][0][1]+1, domain_max),(mapppings[-1][0][1]+1, domain_max)))
    
    
    # if there are gaps _within_ the domains generated above they must also be filled
    i = 0
    while i < len(mapppings) - 1:
        (_, domain_end), (_, _) = mapppings[i]
        (next_domain_start, _), (_, _) = mapppings[i+1]

        if next_domain_start - domain_end > 1:
            gap_mappings.append(((domain_end+1, next_domain_start-1), (domain_end+1, next_domain_start-1)))

        i+=1


    # combine all mappings
    mapppings.extend(gap_mappings)


    # retrieve the list of output ranges
    output_ranges = []
    for c in mapppings:
        output_ranges.append(c[1])

    return output_ranges


def get_lowest_output(start_ranges, converters):
    ranges = start_ranges

    for c in converters:
        new_ranges = []
        for r in ranges:
            subranges = get_ranges(r, c)
            new_ranges.extend(subranges)
        ranges = new_ranges
    
    return sorted(ranges)[0][0]



groups = data.split('\n\n')


seeds = list(map(int, groups[0].split(': ')[1].split()))

converters = []
for g in groups[1:]:
    converter = []
    for line in g.splitlines()[1:]:
        dest, src, n = list(map(int, line.split()))
        src_range = (src, src + n - 1)
        dest_range = (dest, dest + n - 1)
        converter.append((src_range, dest_range))
    converters.append(sorted(converter))


start_ranges = [(s, s) for s in seeds]
start_ranges2 = []
i = 0
while i < len(seeds) - 1:
    start_ranges2.append((seeds[i], seeds[i] + seeds[i+1] - 1))
    i += 2


print("Part 1:", get_lowest_output(start_ranges, converters))
print("Part 2:", get_lowest_output(start_ranges2, converters))
