with open('input.txt') as f:
    data =f.read()


def get_dest_ranges(src_range, transform):
    """
    A transform is a list of mappings, and a mapping is a tuple with a source range nad a destination range.

    This function returns a list of ranges that a given src_range can map to after a given transform.

    It works by splitting src_range into many small ranges, and deciding which destination range they map to,
    before returning only those destination ranges.
    """

    src_min, src_max = src_range


    # this list will eventually contain mappings for all subintervals of src_range
    mapppings = []


    # find all cases where there is an overlap between the input src_range and the src_range of each mapping in the transform
    for mapping in transform:
        (m_src_min, m_src_max), (m_dest_min, m_dest_max) = mapping
        if src_min > m_src_max or src_max < m_src_min:
            # no overlap
            continue

        o_src_min = max(src_min, m_src_min)
        o_src_max = min(src_max, m_src_max)
        o_dest_min = m_dest_min + o_src_min - m_src_min
        o_dest_max = m_dest_min + o_src_max - m_src_min

        mapppings.append(((o_src_min, o_src_max), (o_dest_min, o_dest_max)))


    # if there are no such cases, the entire range should map to itself
    if not mapppings:
        mapppings.append(((src_min, src_max), (src_min, src_max)))
    

    # if there are gaps in the source ranges for the mappings generated above, those gaps must be filled with mappings to itself
    gap_mappings = []


    # if the smallest range start generated above is greater than src_min we must fill that gap
    if mapppings[0][0][0] > src_min:
        gap_mappings.append(((src_min, mapppings[0][0][0]-1),(src_min, mapppings[0][0][0]-1)))
    

    # likewise, if the largest range start generated above is smaller than src_max we must fill that gap
    if mapppings[-1][0][1] < src_max:
        gap_mappings.append(((mapppings[-1][0][1]+1, src_max),(mapppings[-1][0][1]+1, src_max)))
    
    
    # if there are gaps _within_ the ranges generated above they must also be filled
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
    for mapping in mapppings:
        output_ranges.append(mapping[1])

    return output_ranges


def get_lowest_output(start_ranges, transforms):
    ranges = start_ranges

    for t in transforms:
        new_ranges = []
        for r in ranges:
            subranges = get_dest_ranges(r, t)
            new_ranges.extend(subranges)
        ranges = new_ranges
    
    return sorted(ranges)[0][0]



groups = data.split('\n\n')


seeds = list(map(int, groups[0].split(': ')[1].split()))


transforms = []
for g in groups[1:]:
    mappings = []
    for line in g.splitlines()[1:]:
        dest, src, n = list(map(int, line.split()))
        src_range = (src, src + n - 1)
        dest_range = (dest, dest + n - 1)
        mappings.append((src_range, dest_range))
    transforms.append(sorted(mappings))


start_ranges = [(s, s) for s in seeds]
start_ranges_2 = []
i = 0
while i < len(seeds) - 1:
    start_ranges_2.append((seeds[i], seeds[i] + seeds[i+1] - 1))
    i += 2


print("Part 1:", get_lowest_output(start_ranges, transforms))
print("Part 2:", get_lowest_output(start_ranges_2, transforms))
