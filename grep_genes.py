#!/usr/bin/env python3

import argparse
from collections import defaultdict


__author__ = "Ekaterina Osipova, 2021."


def main():
    ## Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--genes', type=str, help='gene list to filter for')
    parser.add_argument('-i', '--isoformes', type=str, help='isoformes file: gene\ttranscript')
    args = parser.parse_args()

    ## Read isoformes into dict
    iso_dict = defaultdict(list)
    with open(args.isoformes, 'r') as inf:
        for line in inf.readlines():
           gene = line.rstrip().split()[0]
           trans = line.rstrip().split()[1]
           iso_dict[gene].append(trans)

    ## Read genes file and output transcripts from dictionary
    with open(args.genes, 'r') as inf:
        for line in inf.readlines():
            g = line.rstrip()
            for t in iso_dict[g]:
                print(t)



if __name__ == "__main__":
    main()
