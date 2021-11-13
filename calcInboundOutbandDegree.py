#!/bin/env -- python3

import numpy as np
import pandas as pd

import sys

# Αν θέλουμε να το εξάγουμε σε latex
latex = True if 'latex' in sys.argv[1:] else False

# Τίτλοι των κόμβων
labels = {0: "G1", 1: "G2", 2: "G3", 3: "G4", 4: "G5", 5: "G6", 6: "G7", 7: "G8", 8: "G9"}


def to_panda(title, lines):
    return pd.DataFrame(columns=['Κόμβος', title],
                        data=map(lambda t: (labels[t[0]], t[1]), enumerate(lines)))


def write_latex(file, df):
    with open(file, "w", encoding='utf-8') as f:
        f.write(df.to_latex(index=False))
        f.flush()


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

outbound = np.sum(adjacency, axis=1)
inbound = np.sum(adjacency, axis=0)

if latex:
    write_latex("outbound.tex", to_panda("Εξερχόμενος βαθμός", outbound))
    write_latex("inbound.tex", to_panda("Εισερχόμενος βαθμός", inbound))
else:
    print(to_panda("Εξερχόμενος βαθμός", outbound).to_csv(index=False))
    print(to_panda("Εισερχόμενος βαθμός", inbound).to_csv(index=False))
