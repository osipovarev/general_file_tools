#!/usr/bin/env python3
#
import argparse
from collections import defaultdict

"""
This script takes a table of values (ID \t value1 \t value 2 \t ...) and finds a minimum.
It output the minimum and the column number with the best value. 
Column=1 means the best value is found in the column next to the ID.
"""

__author__ = "Ekaterina Osipova, 2024."


def main():
    ## Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='table with values per ID: ID \t value1 \t value2 \t value3 ...')
    parser.add_argument('-c', '--cutoff', type=int, default=2, help='the min difference between values to select one over another')
    parser.add_argument('-max', '--max', action='store_true', help='specify if you want to search for max value; default: search for min')
    args = parser.parse_args()

    cutoff = args.cutoff

    ## Parse input table
    with open(args.input, 'r') as inf:
        for line in inf.readlines():
            ID = line.split()[0]
            values = [float(i) for i in line.split()[1:]]

            if args.max:
                values = [-i for i in values]
            for i, v in enumerate(values):
                if i == 0:
                    v_min = v
                    n = i
                else:
                    if v_min - v > cutoff:
                        v_min = v
                        n = i
            if args.max:
                print('{}\t{}\t{}'.format(ID, -v_min, n+1))    
            else:
                print('{}\t{}\t{}'.format(ID, v_min, n+1))
    		

if __name__ == "__main__":
    main()
