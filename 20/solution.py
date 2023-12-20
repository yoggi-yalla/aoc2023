import math

with open('input.txt') as f:
    data = f.read()


modules = {}

for line in data.splitlines():
    a, b = line.split(' -> ')
    dests = b.split(', ')

    t = a[0]    
    n = a[1:] if t in ('%', '&') else a

    modules[n] = [t, 0, dests]


for k, v in modules.items():
    t, s, d = v
    if t == '&':
        modules[k][1] = {}
        for kk, vv in modules.items():
            if k != kk:
                tt, ss, dd = vv
                if k in dd:
                    modules[k][1][kk] = 0


lowest = {}


def send_pulse(low_high, src, dest, i):
    if low_high == 1 and dest == 'nr' and src not in lowest:
        lowest[src] = i

    if dest not in modules:
        return []
    
    t, s, d = modules[dest]

    buffer = []

    if t == '%':
        if low_high == 0:
            modules[dest][1] = 1 - modules[dest][1]
            for dd in d:
                buffer.append((modules[dest][1], dest, dd))
    
    elif t == '&':
        modules[dest][1][src] = low_high
        if all(v == 1 for v in modules[dest][1].values()):
            out = 0
        else:
            out = 1
        for dd in d:
            buffer.append((out, dest, dd))
    
    else:
        for dd in d:
            buffer.append((low_high, dest, dd))
    
    return buffer


hc = 0
lc = 0

def push_button(i):
    global hc, lc

    buffer = [(0, 'button', 'broadcaster')]

    next_buffers = [buffer]

    while next_buffers:
        buf = next_buffers.pop(0)
        while buf:
            low_high, src, dest = buf.pop(0)
            if low_high > 0: 
                hc += 1
            else: 
                lc += 1
            next_buffers.append(send_pulse(low_high, src, dest, i))


for i in range(1, 1_000_000):
    push_button(i)

    if i == 1000:
        print("Part 1:", hc*lc)
    if len(lowest) == 4:
        print("Part 2:", math.prod(lowest.values()))
        break
