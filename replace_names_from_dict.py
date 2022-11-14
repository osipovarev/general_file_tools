#!/usr/bin/env python3


"""
This script takes an annotation file and replaces/adds
prefix/ suffix to names in the requested field
"""

import argparse
from collections import defaultdict
import sys


__author__ = "Ekaterina Osipova, 2021."


def read_anno_into_dict(anno, field, split_symbol, ignore):
    ## Reads an annotation file into a dictionary

    anno_dict = defaultdict(list)
    with open(anno, 'r') as inf:
        for line in inf.readlines():
            if split_symbol == ',':
                all_fields = line.rstrip().split(split_symbol)
            else:
                all_fields = line.rstrip().split()
            if len(all_fields) < field - 1:
                print('There is no field {} in the annotation! Abort'.format(field))
                sys.exit(1)
            else:
                id = all_fields[field - 1]
                transc_info = line.rstrip()
                if ignore:
                    id_suff = id.split('.')[-1]
                    id_core = '.'.join(id.split('.')[:-1])
                    anno_dict[id_core].append(transc_info)
                else:
                    anno_dict[id].append(transc_info)
    return anno_dict


def read_renaming_dict(file):
    ## Reads correspondence table into a dictionary

    rename_table = {}
    with open(file, 'r') as inf:
        for line in inf.readlines():
            rename_table[line.split(',')[0]] = line.rstrip().split(',')[1]
    return rename_table


def rename_ids(anno_dict, rename_table, prefix=False, suffix=False):
    ## Renames or labels IDs in the annotation

    for t in anno_dict:
        if t in rename_table:
            new_name = rename_table[t]
            # if ignore:
            #     id_suff = anno_dict[t][0]
            #     new_name += ".{}".format(id_suff)
            
            if prefix:
                prefix = new_name + '_'
                new_t = prefix + t.replace(prefix, '')
            elif suffix:
                suffix = '_' + new_name
                new_t = t.replace(suffix, '') + suffix
            else:
                new_t = new_name
            
            for transc in anno_dict[t]:
                print(transc.replace(t, new_t))
        else:
            for transc in anno_dict[t]:
                print(transc)


def main():
    ## Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--name_dict', type=str, help='dictionary with replacements in csv format: nameOld,nameNew')
    parser.add_argument('-a', '--anno', type=str, help='annotation file')
    parser.add_argument('-p', '--prefix', action='store_true',
                        help='specify if you dont want to replace names entirely, just to add a prefix from the dictionary')
    parser.add_argument('-s', '--suffix', action='store_true',
                        help='specify if you dont want to replace names entirely, just to add a suffix from the dictionary')
    parser.add_argument('-f', '--field', type=int, default=4, help='field number to label; default=4(transciprt_ID in bed12)')
    parser.add_argument('-c', '--comma', action='store_true', help='specify if anno file is comma separated (.csv)')
    parser.add_argument('-i', '--ignore', action='store_true', help='specify if anno IDs have suffixes you want to ignore')
    args = parser.parse_args()

    ## bed12 format:
    ## chrom[0] start[1] end[2] name[3] score[4] strand[5] cds_start[6] cds_end[7] rgb[8] count[9]\
    ##  block_sizes[10] block_starts[11]

    ## Read annotation into a dictionary: {transc_id : transc_info}
    split_symbol = ''
    if args.comma:
        split_symbol = ','
    anno_dict = read_anno_into_dict(args.anno, args.field, split_symbol, args.ignore)

    ## Read file with name replacements
    rename_table = read_renaming_dict(args.name_dict)

    ## Give labels or rename IDs in the annotation file
    rename_ids(anno_dict, rename_table, args.prefix, args.suffix)


if __name__ == '__main__':
    main()
