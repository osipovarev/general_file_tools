#!/usr/bin/env python3
#
import argparse
from collections import defaultdict
import sys


__author__ = "Ekaterina Osipova, 2022."

def read_obo_to_dict(file, delimiter):
    ## Reads GO graph file in obo format into a dictionary

    obo_dict_children = defaultdict(list)
    obo_dict_parents = {}

    with open(file, 'r') as inf:
        all_entries = inf.read().strip().split(delimiter)
        for entry in all_entries:
            if entry != '':
                all_attributes = entry.rstrip('\n').split('\n')
                go_parents = []
                for attribute in all_attributes:
                    if attribute.startswith('id:'):
                        go = attribute.split(': ')[1]
                    elif attribute.startswith('name:'):
                        go_name = attribute.split(': ')[1]
                    elif attribute.startswith('is_a:'):
                        go_parent = attribute.split()[1]
                        go_parents.append(go_parent)
                    elif attribute.startswith('relationship: part_of'):
                        go_part_of = attribute.split()[2]
                        go_parents.append(go_part_of)

                obo_dict_parents[go] = (go_name, go_parents)
                for parent in go_parents:
                    obo_dict_children[parent].append((go, go_name))
    return obo_dict_parents, obo_dict_children


def main():
    ## Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fileobo', type=str, help='go.obo file to parse')
    parser.add_argument('-go', '--go', type=str, help='GO term to get children, e.g: GO:0061061')
    parser.add_argument('-c', '--children', action='store_true', help='specify to get children of the GO')
    parser.add_argument('-p', '--parents', action='store_true', help='specify to get parents of the GO')
    parser.add_argument('-l', '--listparents', type=str, default='', help='check if requested GO has parents from the list')
    args = parser.parse_args()

    ## Read obo file with GO
    delimiter = "[Term]"
    obo_dict_parents, obo_dict_children = read_obo_to_dict(args.fileobo, delimiter)


    ## Output children of requested GO term
    go = args.go
    if args.children:
        for term in obo_dict_children[go]:
            print('{}\t{}'.format(term[0], term[1]))
    if args.parents:
        term = obo_dict_parents[go]
        print('{}\t{}\nparents:\t{}'.format(go, term[0], ','.join(term[1])))


    ## Check parents in the list
    parents_line = args.listparents
    if parents_line != '':
        parents_list = parents_line.split(',')
        term = obo_dict_parents[go]
        intersect_parents = list(set(term[1]) & set(parents_list))
        if intersect_parents == []:
            print('{} has no parents from the list'.format(go))
        else:
            print('{} has parents in the list: {}'.format(go, intersect_parents))



if __name__ == "__main__":
        main()