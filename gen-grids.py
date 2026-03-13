#!/usr/bin/env python3
"""Generate random multiplication grid puzzles with uniform distribution.

Precomputes all valid (a,b,c,d) tuples where all four products <= 20,
then samples uniformly from that set.

Output: grids.tex with layout commands for multgrid.tex.
Prints cell and constraint value frequencies to stdout.
"""

import random
from collections import Counter

MAX_PRODUCT = 20
CELL_MAX = 10
COLS = 3
ROWS = 3
GRIDS_PER_PAGE = COLS * ROWS
PAGES = 5
TOTAL = GRIDS_PER_PAGE * PAGES

# Build list of all valid tuples
valid = []
for a in range(CELL_MAX + 1):
    for b in range(CELL_MAX + 1):
        if a * b > MAX_PRODUCT:
            continue
        for c in range(CELL_MAX + 1):
            if a * c > MAX_PRODUCT:
                continue
            for d in range(CELL_MAX + 1):
                if c * d > MAX_PRODUCT or b * d > MAX_PRODUCT:
                    continue
                valid.append((a, b, c, d))

# Count how often each constraint value appears across all valid tuples
constraint_freq = Counter()
for a, b, c, d in valid:
    constraint_freq.update([a * b, c * d, a * c, b * d])

# Weight each tuple inversely by frequency of its constraint values,
# so rare constraints (like primes > 10) get boosted.
# Use square root to soften the weighting — fully inverse is too aggressive
# (eliminates 0s entirely).
weights = []
for a, b, c, d in valid:
    w = 1.0 / (constraint_freq[a * b] * constraint_freq[c * d]
                * constraint_freq[a * c] * constraint_freq[b * d]) ** 0.5
    # Penalize tuples with duplicate constraint values
    constraints = [a * b, c * d, a * c, b * d]
    unique = len(set(constraints))
    if unique < 4:
        w *= 0.3 ** (4 - unique)
    weights.append(w)

# Sample
grids = random.choices(valid, weights=weights, k=TOTAL)

# Write grids.tex
with open("grids.tex", "w") as f:
    for page in range(PAGES):
        if page > 0:
            f.write("\\newpage\n\\startpage\n")
        for row in range(ROWS):
            idx = page * GRIDS_PER_PAGE + row * COLS
            items = []
            for col in range(COLS):
                a, b, c, d = grids[idx + col]
                items.append(f"\\grid{{{a}}}{{{b}}}{{{c}}}{{{d}}}")
            f.write("\\makebox[\\textwidth]{%\n")
            f.write("\\hfill".join(items) + "%\n")
            f.write("}\n")
            if row < ROWS - 1:
                f.write("\n\\vspace{1.5cm}\n\n\\noindent\n")

# Print frequency stats
cell_counts = Counter()
constraint_counts = Counter()
for a, b, c, d in grids:
    cell_counts.update([a, b, c, d])
    constraint_counts.update([a * b, c * d, a * c, b * d])

print(f"{len(valid)} valid tuples in pool")
print("Cell values:")
for v in range(CELL_MAX + 1):
    print(f"  {v:2d}: {cell_counts[v]}")
print("Constraint values:")
for v in range(MAX_PRODUCT + 1):
    print(f"  {v:2d}: {constraint_counts[v]}")

# Count grids with duplicate constraints
dup_count = 0
for a, b, c, d in grids:
    constraints = [a * b, c * d, a * c, b * d]
    if len(set(constraints)) < 4:
        dup_count += 1
print(f"Grids with duplicate constraints: {dup_count}/{TOTAL}")
