#!/usr/bin/env python3

import argparse
import pandas as pd
from scipy.stats import fisher_exact


__author__ = "Ekaterina Osipova, 2024."


def read_file(file_path):
    with open(file_path, 'r') as file:
        return set(file.read().splitlines())


def fisher_exact_test(universe, category1, group1):
    # Calculte category 2 and group 2
    category2 = universe - category1
    group2 = universe - group1

    # Calculate 2-by-2 table
    c1_g1 = universe & category1 & group1
    c1_g2 = universe & category1 & group2
    c2_g1 = universe & category2 & group1
    c2_g2 = universe & category2 & group2

    table = [
        [len(c1_g1), len(c1_g2)],
        [len(c2_g1), len(c2_g2)]
            ]

    # Perform Fisher exact test
    odds_ratio, p_value = fisher_exact(table, alternative='two-sided')

    return (len(c1_g1), len(c1_g2), len(c2_g1), len(c2_g2)), p_value


def main():
    ## Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--universe', type=str, help='total list of elements aka universe')
    parser.add_argument('-l1', '--list1', type=str, help='list of elements with category 1')
    parser.add_argument('-l2', '--list2', type=str, help='list of elements with GROUP 1')
    parser.add_argument('-t', '--table', action='store_true', help='specify the flag if you also want to output the numbers in the table')
    args = parser.parse_args()

    # Read sets from files
    universe = read_file(args.universe)
    category1 = read_file(args.list1)
    group1 = read_file(args.list2)

    # Perform Fisher exact test
    (c1_g1, c1_g2, c2_g1, c2_g2), p_value = fisher_exact_test(universe, category1, group1)

    # Output values in the table if requested
    if args.table:
        print((c1_g1, c1_g2, c2_g1, c2_g2))

    # Output the p-value
    print(f"P-Value from Fisher Exact Test: {p_value}")


if __name__ == "__main__":
    main()

