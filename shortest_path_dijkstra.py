cables_info = [
    (0, 500),
    (600, 9100),
    (1000, 2000),
    (2500, 3500),
    (3000, 4500),
    (3000, 5500),
    (4800, 5500),
    (5000, 7000),
    (5500, 7000),
    (7000, 9000),
    (8000, 9500),
    (5800, 7500),
    (9000, 9990)
]

starts_at = 0
ends_at = 10000


every_nodes = [starts_at, ends_at]
for st, ed in cables_info:
    every_nodes.append(st)
    every_nodes.append(ed)

every_nodes = set(every_nodes)
every_nodes = sorted(list(every_nodes))

# print(every_nodes)

every_edges = []
startings = every_nodes[:-1]
endings = every_nodes[1:]
for st, ed in zip(startings, endings):
    forward = [st, ed, ed-st]
    backward = [ed, st, ed-st]
    every_edges.append(forward)
    every_edges.append(backward)

for st, ed in cables_info:
    dir_edge = [st, ed, 0]
    every_edges.append(dir_edge)

# for edge in every_edges:
#     print(edge)

distances = {}
for n in every_nodes:
    distances[n] = ends_at + 1
distances[0] = 0

path = {}
while len(every_nodes) > 0:
    for node, dist in sorted(distances.items(), key=lambda x: x[1]):
        if node in every_nodes:
            break

    every_nodes.remove(node)

    for start, end, length in every_edges:
        if start == node:
            if distances[end] > length + dist:
                distances[end] = length + dist
                path[end] = node

for key, value in sorted(distances.items(), key=lambda x: x[0]):
    print(key, value)

print('=======================')
print(path)
shortest = [ends_at]
while shortest[-1] != starts_at:
    prev = path[shortest[-1]]
    shortest.append(prev)

print(shortest[::-1])
