#!/usr/bin/env python3
#
import argparse
from collections import defaultdict


__author__ = "Ekaterina Osipova, 2022."


def read_into_dict(file):
    ## Read file into dict

    iso_dict = defaultdict(list)
    with open(file, 'r') as inf:
        for line in inf.readlines():
           g = line.rstrip().split()[0]
           t = line.rstrip().split()[1]
           iso_dict[g].append(t)
    return iso_dict


def main():
    ## Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-d1', '--dict1', type=str, help='dict file 1: gene \t transcript')
    parser.add_argument('-d2', '--dict2', type=str, help='dict file 2: gene \t transcript')
    args = parser.parse_args()

	## Read both dict files
	dict1 = read_into_dict(args.dict1)
	dict2 = read_into_dict(args.dict2)

    ## Print corresponding elements side by side
    for g in dict1:
    	if g in d2:
    		print('{}\t{}\t{}'.format(g, d1[g], d2[g]))
    	else:
    		print('{}\t{}\t{}'.format(g, d1[g], 'Not_found'))
    		

if __name__ == "__main__":
    main()