#!/usr/bin/env python3
import sys
from statsmodels.stats.multitest import multipletests

# Read newline-separated p-values from stdin
pvals_all = sys.stdin.read()
pvals = pvals_all.split("\n")

# FDR correction
fdr = multipletests([float(p) for p in pvals if p != ''], method="fdr_bh")[1]

# Print adjusted p-values to stdout
for val in fdr:
    print(val)
