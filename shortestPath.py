#!/bin/env -- python3

import networkx as nx
import numpy as np

# Τίτλοι των κόμβων
labels = {0: "G1", 1: "G2", 2: "G3", 3: "G4", 4: "G5", 5: "G6", 6: "G7", 7: "G8",
          8: "G9"}

# Ενας πίνακας γειτνίασης 
adjacency = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 0]
])
# Δινουμε τον πίνακα γειτνίασης στο networkx
# σαν κατευθυνόμενος γράφος
gr = nx.MultiDiGraph(incoming_graph_data=adjacency)
shortestPathSamples = {}
path_lengths = nx.shortest_path_length(gr)
for sourceNode, targets in path_lengths:
    for targetNode in targets:
        length = targets[targetNode]
        if 4 > length > 0:
            if length not in shortestPathSamples:
                shortestPathSamples[length] = [sourceNode, targetNode]

for key, item in shortestPathSamples.items():
    shortPath = nx.shortest_path(gr, source=item[0], target=item[1])
    print("Length: {}, Path: {}".format(key, ", ".join(list(map(lambda s: labels[s], shortPath)))))
