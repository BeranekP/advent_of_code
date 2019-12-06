import networkx as nx
import matplotlib.pyplot as plt
FILE = 'input.txt'
with open(FILE, 'r') as f:
    planets = dict(reversed(orbit.split(')'))
                   for orbit in f.read().splitlines())


G = nx.Graph()

for k, v in planets.items():
    G.add_node(k)
    G.add_edge(k, v)

source = 'COM'
path = nx.single_source_shortest_path_length(G, source)
print(f'Number of orbits : {sum(list(path.values()))}')

for path in nx.all_simple_paths(G, source='YOU', target='SAN'):
    print(f'Orbital jumps to Santa: {len(path)-3}')
# view network
size = []
color = []
for node in G.nodes:
    s = 150 if node == 'SAN' or node == 'YOU' else 10
    c = 'red' if node == 'SAN' or node == 'YOU' else 'blue'
    size.append(s)
    color.append(c)

nx.draw(G, with_labels=True, node_size=size, font_size=6, node_color=color)
plt.show()
