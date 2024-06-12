#!/usr/bin/env python3
#
# This script takes two files with sets of elements in format element \n \
# and outputs what is in the first set but not in the second; what is not in the second but in the first; \
# length of these differences between two sets.

import argparse


__author__ = "Ekaterina Osipova, 2018."


parser = argparse.ArgumentParser()
parser.add_argument('-f1', '--fileone', type=str, help='file with first set of elements')
parser.add_argument('-f2', '--filetwo', type=str, help='file with second set of elements')
parser.add_argument('-n', '--newline', action='store_true', help='if specified, output every element as a separate line')
args = parser.parse_args()


with open(args.fileone, 'r') as fone:
    lines = fone.readlines()
    first_list = map(str.strip, lines)

with open(args.filetwo, 'r') as ftwo:
    lines = ftwo.readlines()
    second_list = map(str.strip, lines)


seen = set()
seenAdd = seen.add
uniq_first = [x for x in second_list if not (x in seen or seenAdd(x))]
seen = set()
seenAdd = seen.add
uniq_second = [x for x in first_list if not (x in seen or seenAdd(x))]

gain_list = list(set(uniq_second) - set(uniq_first))
loss_list = list(set(uniq_first) - set(uniq_second))

print('## number of elements NOT in f2: {}'.format(len(list(set(uniq_second) - set(uniq_first)))))
print('## number of elements NOT in f1: {}'.format(len(list(set(uniq_first) - set(uniq_second)))))
if args.newline:
    print('## Elements NOT in f2:')
    for i in gain_list: print(i)
    print('## Elements NOT in f1:')
    for i in loss_list: print(i)
else:
    print('## Elements NOT in f2:')
    print(*gain_list)
    print('## Elements NOT in f1:')
    print(*loss_list)
