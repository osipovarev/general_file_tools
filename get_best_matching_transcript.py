#!/usr/bin/env python3
#
import argparse
from collections import defaultdict
import numpy as np


__author__ = "Ekaterina Osipova, 2020."


def get_bases(starts, sizes):
    ## Converts provided intervals into lists of bases

    list_2d = [list(range(starts[i], starts[i] + sizes[i])) for i in range(len(starts))]
    return list(np.concatenate(list_2d))


def read_bed25_lines(file):
    ##

    match_dict = defaultdict(list)
    ## bed12 format:
    ## chrom[0] start[1] end[2] name[3] score[4] strand[5] cds_start[6] cds_end[7] rgb[8] count[9]\
    ##  block_sizes[10] block_starts[11]
    with open(file, 'r') as inf:
        for line in inf.readlines():
            a_bed = line.split()[:12]
            b_bed = line.split()[12:25]
            a_name = a_bed[3]
            b_name = b_bed[3]

            a_starts = [int(i) for i in a_bed[11].rstrip(',').split(',')]
            b_starts = [int(i) for i in b_bed[11].rstrip(',').split(',')]
            a_block_sizes = [int(i) for i in a_bed[10].rstrip(',').split(',')]
            b_block_sizes = [int(i) for i in b_bed[10].rstrip(',').split(',')]
            a_bases = get_bases(a_starts, a_block_sizes)
            b_bases = get_bases(b_starts, b_block_sizes)

            bases_overlap = len(list(set(a_bases) & set(b_bases)))
            a_delta = 1.0 - float(bases_overlap) / float(len(a_bases))
            b_delta = 1.0 - float(bases_overlap) / float(len(b_bases))
            fine = a_delta + b_delta

            match_dict[a_name].append((b_name, fine))
    return match_dict


def find_best_match(match_dict):
    ## For each A transcript find best matching (=lowest fine) transcript B from match dict
    for a in match_dict:
        best_match = min(match_dict[a], key=lambda t: t[1])
        print('{}\t{}'.format(a, best_match[0]))


def main():
    ## Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--transcriptmatch', type=str, help='bed25 file of matching transcripts: a,b from bedtools intersect')
    args = parser.parse_args()

    ## Read each bed12+bed12 line into transcript dictionary with coverage of A and B
    match_dict = read_bed25_lines(args.transcriptmatch)

    ## Find the best matching transcript (=lowest fine)
    find_best_match(match_dict)


if __name__ == "__main__":
    main()
