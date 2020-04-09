#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-08
Purpose: Probabalistically subset FASTA files
"""

import argparse
import os
import sys
import random
from Bio import SeqIO



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probabalistically subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input FASTA file(s)')

    parser.add_argument('-p',
                        '--pct',
                        help='Percent of reads',
                        metavar='reads',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')


    args = parser.parse_args()

    if not 0 <= args.pct <= 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')
    
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    num_sequence = 0
    total_num_files = 0

    for num_file, fh in enumerate(args.file, start=1):
        basename = os.path.basename(fh.name)
        out_file = os.path.join(args.outdir, basename)
        print(f'{num_file:3}: {basename}')
        total_num_files += 1

        out_fh = open(out_file, 'wt')
        for rec in SeqIO.parse(fh, 'fasta'):
            if random.random() <= args.pct:
                SeqIO.write(rec, out_fh, 'fasta')
                num_sequence += 1

        out_fh.close()

    word_sequence = 'sequence' if num_sequence == 1 else 'sequences'
    word_file = 'file' if total_num_files ==1 else 'files'
    print(f'Wrote {num_sequence:,} {word_sequence} from {total_num_files} {word_file} to directory "{args.outdir}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
