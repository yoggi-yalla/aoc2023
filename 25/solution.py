import networkx as nx
from pyvis.network import Network
from collections import defaultdict


def load_connections(path):
    connections = defaultdict(list)

    for line in open(path).readlines():
        f, t = line.split(': ')

        for tt in t.split():
            connections[f].append(tt)
            connections[tt].append(f)
    
    return connections

c1 = load_connections('input.txt')

G = nx.Graph()
for f, t in c1.items():
    for tt in t:
        G.add_edge(f, tt)

net = Network(notebook=True)
net.from_nx(G)
net.show('graph.html')


c2 = load_connections('modified_input.txt')

def count(node, connections):
    seen = set()
    q = [node]
    ans = 0
    while q:
        node = q.pop()
        
        if node in seen:
            continue
        seen.add(node)

        for nn in connections[node]:
            q.append(nn)
        
        ans += 1
    
    return ans

print("Part 1&2:", count('chr', c2) * count('cpq', c2))
