#!/bin/env -- python3

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import sys

# Αν θέλουμε να το εξάγουμε σε latex
latex = True if 'latex' in sys.argv[1:] else False

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
# Χρησιμοποιούμε κυκλικό πλάνο γιατί έχουμε πολλές ακμές
pos = nx.circular_layout(gr)
# δημιουργούμε το γράφημα
nx.draw(gr, pos, node_size=2100, labels=labels, with_labels=True, font_size=10, font_color="whitesmoke")

# αν έχουμε επιλέξει να το γράψουμε σαν αρχείο την ενσωμάτωση σε latex ή
# απλά εμφάνιση
if latex:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.savefig('graphic1.pgf')
else:
    plt.show()
