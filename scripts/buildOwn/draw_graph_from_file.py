import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object
G = nx.Graph()

# Read edges from the text file
with open('edges.txt', 'r') as file:
    for line in file:
        node1, node2, weight = line.split()
        G.add_edge(node1, node2, weight=float(weight))

# Get edge weights for drawing
edge_labels = nx.get_edge_attributes(G, 'weight')

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_color='black', edge_color='gray')

# Draw edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Network Graph from Text File")
plt.show()
