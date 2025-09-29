#!/usr/bin/env python3

import argparse
from Bio import AlignIO

__author__ = "chatgpt, 2025."



def get_sequences_from_maf_record(record):
    # Each MAF block has 2 seq records
    # They are in block's 'seqs'
    s1, s2 = str(record[0].seq).upper(), str(record[1].seq).upper()
    src1 = record[0].id
    src2 = record[1].id
    start1 = int(str(record[0].annotations['start']))
    start2 = int(str(record[1].annotations['start']))
    return s1, s2, src1, src2, start1, start2


def maf_blocks_to_identity_windows(maf_file, window_size, step):
    # Dict: {chrom : [(pos, bp_callable, bp_diff)]}
    windows = {}
    for record in AlignIO.parse(maf_file, "maf"):
        s1, s2, src1, src2, start1, start2 = get_sequences_from_maf_record(record)
        # For simplicity, assume src1 = chrom
        chrom = src1.split('.')[0] if '.' in src1 else src1
        chrom_len = max(len(s1), len(s2))  # conservative length
        seq1_pos, seq2_pos = start1, start2
        
        if chrom not in windows:
            windows[chrom] = {}
        
        for i in range(len(s1)):
            base1, base2 = s1[i], s2[i]
            # Bases are aligned; increase position if not a gap
            if base1 not in '-N' and base2 not in '-N':
                pos = seq1_pos  # Just pick one genome's coordinate
                widx = pos // step
                if widx not in windows[chrom]:
                    windows[chrom][widx] = {'bp_callable': 0, 'bp_diff': 0}
                windows[chrom][widx]['bp_callable'] += 1
                if base1 != base2:
                    windows[chrom][widx]['bp_diff'] += 1
            if base1 not in '-':
                seq1_pos += 1
            if base2 not in '-':
                seq2_pos += 1
    
    # Output
    for chrom in sorted(windows):
        for widx in sorted(windows[chrom]):
            start = widx * step
            end = start + window_size
            bp_callable = windows[chrom][widx]['bp_callable']
            bp_diff = windows[chrom][widx]['bp_diff']
            p_hat = bp_diff / bp_callable if bp_callable else None
            print(f"{chrom}\t{start}\t{end}\t{bp_callable}\t{bp_diff}\t{p_hat}")


def main():
    ## Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--maf', type=str, help='name of the input maf file')
    args = parser.parse_args()

    window_size = 100_000
    step = 100_000

    maf_blocks_to_identity_windows(args.maf, window_size, step)


if __name__ == "__main__":
    main()
