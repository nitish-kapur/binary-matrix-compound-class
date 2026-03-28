"""
Compound Class Visual Representation
Copyright (C) 2026 Nitish Kapur
GitHub: [github.com/nitish-kapur](https://github.com/nitish-kapur)
Licensed under GNU GPLv3
"""
"""
    This script was made as a part of a biofuel research project.

    1.  Defines a mapping of wavenumber region keys to the sample categories
        in which each corresponding compound class is detected.
    2.  Defines a mapping of the same keys to human-readable compound class
        names (e.g. "Alkanes", "Aromatics", "Phenols, ethers, acids").
    3.  Sorts each sample category list alphabetically and removes duplicates.
    4.  Builds a pandas DataFrame combining the wavenumber key, compound class
        name, and associated sample categories for each entry.
    5.  Sorts the DataFrame alphabetically by compound class name.
    6.  Constructs a binary matrix where rows are compound classes and columns
        are sample categories; a cell is 1 (present) or 0 (absent).
    7.  Renders the binary matrix as a heatmap using a custom two-colour
        colormap: green for presence (1) and red for absence (0).
    8.  Overlays a dashed black grid to delineate individual cells clearly.
    9.  Saves the heatmap as 'binaryMatrixRedGreen_.png' and displays it
        interactively.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.colors as mcolors

# Custom colormap: red for absence (0), green for presence (1)
colors = ["#c10000", "#10d133"]  # Red for 0 (absence), Green for 1 (presence)
cmap = mcolors.ListedColormap(colors)
bounds = [0, 0.5, 1]
norm = mcolors.BoundaryNorm(bounds, cmap.N)

print(os.getcwd())

# Mapping and compound classes (with hyphens normalized)
mapping = {
    "1": ["DW","E20 Petrol","Ethanol","OH","WW"],
    "2": ["Diesel","E20 Petrol","Ethanol","Kerosene","W","WL","WW","D SUM","DW","D WIN","OH"],
    "3": ["OH","D WIN", "WL", "WW","DW"],
    "4": ["DW", "OH", "WW"],
    "5": ["Diesel","E20 Petrol","Kerosene","WL","D SUM","W","WW","DW","D WIN", "OH"],
    "6": ["DW","OH","WW"],
}

compound_classes = {
    "1": "Alcohol, phenol, water",
    "2": "Alkanes",
    "3": "Alkenes",
    "4": "Aldehydes, carboxylic acids, ketones",
    "5": "Aromatics",
    "6": "Phenols, ethers, acids",
}

# Sort sample categories
mapping_sorted = {k: sorted(list(set(v))) for k,v in mapping.items()}

# Build dataframe
df = pd.DataFrame([
    [k, compound_classes.get(k, "Unknown"), ", ".join(mapping_sorted[k])]
    for k in mapping_sorted
], columns=["Wavenumber","Compound Class","Sample Categories"])

# Sort the DataFrame by the "Compound Class" alphabetically
df_sorted = df.sort_values(by="Compound Class").reset_index(drop=True)

# Custom order of categories (updated)
custom_order = ["WL", "D SUM", "D WIN", "Kerosene", "Diesel", "E20 Petrol", "W", "WW", "DW", "OH"]
# categories = custom_order
categories = sorted(custom_order)

# Construct binary matrix for the sorted DataFrame
matrix_sorted = np.zeros((len(df_sorted), len(categories)), dtype=int)

for i, row in df_sorted.iterrows():
    cats = mapping_sorted[row["Wavenumber"]]
    for j, cat in enumerate(categories):
        matrix_sorted[i][j] = 1 if cat in cats else 0

# Create heatmap with sorted y-axis
plt.figure(figsize=(18,9))
plt.imshow(matrix_sorted, aspect='auto', cmap=cmap, norm=norm)
plt.xticks(range(len(categories)), categories, rotation=90, fontsize=16)
plt.yticks(range(len(df_sorted)), df_sorted["Compound Class"], fontsize=16)

# Draw dashed grid lines
for x in range(len(categories)+1):
    plt.axvline(x-0.5, color='black', linestyle='--', linewidth=1)
for y in range(len(df_sorted)+1):
    plt.axhline(y-0.5, color='black', linestyle='--', linewidth=1)

plt.tight_layout()
plt.savefig("binaryMatrixRedGreen_.png")
plt.show()
plt.close()
