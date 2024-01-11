#!/usr/bin/env python3

import argparse
import itertools


__author__ = "Ekaterina Osipova, 2024."


def main():
    ## Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-l1', '--list1', type=str, help='comma-separated list of elements 1')
    parser.add_argument('-l2', '--list2', type=str, help='comma-separated list of elements 2')
    args = parser.parse_args()

    l1 = args.list1.rstrip(',').split(',')
    l2 = args.list2.rstrip(',').split(',')

    for pair in list(itertools.product(l1, l2)):
        print('{} {}'.format(pair[0], pair[1]))


if __name__ == "__main__":
    main()