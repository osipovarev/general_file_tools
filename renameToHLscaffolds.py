#!/usr/bin/env python3

# this script replaces name of scaffold/chroms in the fist column of the annotation file (format does not matter)
# with corresponding scaffold/chroms names from the renaming_dictionary.csv file
# writes to stdout

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--annofile', type=str, help='annotation file; 1st columns - scaffolds/chroms names')
parser.add_argument('-d', '--renamedict', type=str, help='table of name correspondence, usually renaming_dictionary.csv')
parser.add_argument('-c', '--column', type=int, default=1, help='column to rename; default 1')
parser.add_argument('-s', '--sep', type=str, default='\t', help='specify field separator of the anno file; default=tab')
args = parser.parse_args()

# read correspondence table into dictionary
rename_table = {}
with open(args.renamedict, 'r') as inf:
    for line in inf.readlines():
        rename_table[line.split(',')[0]] = line.rstrip('\n').split(',')[1]


# read annotation file, replace requested column
ncol = args.column
sep = args.sep
with open(args.annofile, 'r') as inf:
    for line in inf.readlines():
        line = line.rstrip()
        l = line.split(sep)
        if len(l) < ncol - 1:
            print(line)
        else:
            old_id = l[ncol - 1]
            if old_id in rename_table:
                new_id = rename_table[old_id]
            else:
                new_id = old_id
            new_line = sep.join(l[ :ncol - 1] + [new_id] +  l[ncol: ])
            print(new_line)


