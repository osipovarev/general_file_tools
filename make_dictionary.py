#!/usr/bin/env python3
#
import argparse
from collections import defaultdict


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, help='file with two columns; e.g: ENSGALG000\tENSGALT000')
parser.add_argument('-c', '--comma', action='store_true', help='specify if file is ENSG\tENST1,ENST2, format')
args = parser.parse_args()

d = defaultdict(list)
# read file into dictionary
with open(args.file, 'r') as inf:
    for line in inf.readlines():
        id1 = line.split()[0]
        id2 = line.split()[1]
        if args.comma:
            for t in id2.rstrip(',').split(','):
                d[id1].append(t)
        else:
            d[id1].append(id2)

# output dictionary structure
for id1 in d:
    if args.comma:
        for t in d[id1]:
            print('{}\t{}'.format(id1, t))
    else:
        id2_line = ','.join(d[id1])
        print('{}\t{}'.format(id1, id2_line))
