#!/usr/bin/env python
#
# This script takes files with set of elements in format element \n \
# and outputs elements in intersection; \
import argparse


__author__ = "Ekaterina Osipova, 2019."


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filelist', nargs='*', type=str, help='list of files to find intersection')
args = parser.parse_args()


file_list = args.filelist
# initiate a 2D list to store lists of elements from each file
allElements_allFiles = []

for file in file_list:
    with open(file, 'r') as inf:
        lines = inf.readlines()
        elements_in_file = map(str.strip, lines)
        allElements_allFiles.append(elements_in_file)

overlapping_elements = set(allElements_allFiles[0]).intersection(*allElements_allFiles)

# output overlapping elements
for el in overlapping_elements:
    print(el)
