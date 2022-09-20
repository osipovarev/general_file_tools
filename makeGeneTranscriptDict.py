#!/usr/bin/env python
#
# This script takes a file geneID{\t}transcriptID 
# and outputs a file with lines looking like: GENENAME\tTRANSC1,TRANSC2,...etc

import argparse
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('-id', '--ids', type=str, help='file name with geneID\ttranscriptID table')
parser.add_argument('-o', '--output', type=str, help='output file name')
args = parser.parse_args()

d = defaultdict(list)
inf = open(args.ids, 'r')
allLines = inf.readlines()
for line in allLines:
    gene = line.split()[0]
    transc = line.split()[1]
    d[gene].append(transc)
inf.close()

with open(args.output, 'w') as ouf:
    for key in d:
	ouf.write(key)
	ouf.write('\t')
        ouf.write(','.join(d[key]))
        ouf.write('\n')
