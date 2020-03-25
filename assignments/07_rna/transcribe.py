#!/usr/bin/env python3
"""
Author : khlopez08
Date   : 2020-03-24
Purpose: Transcribing DNA into RNA
"""

import argparse
import os
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribing DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()
    
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
        
    return args


# --------------------------------------------------
def main():
    """The Imperial March sounds"""

    args = get_args()
    out_dir = args.outdir
    codon = 'U'
    sequence_count = 0
    
    for fh in args.file:
        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        for line in fh:
            sequence_count += 1
            dna_sequence = line.split()
            rna_sequence = dna_sequence[0].replace('T', codon)
            out_fh.write(rna_sequence + '\n')
            
    word = 'sequence' if sequence_count == 1 else 'sequences'
    transcription_file = 'file' if len(args.file) == 1 else 'files'
    print(f'Done, wrote {sequence_count} {word} in {len(args.file)} {transcription_file} to directory "{out_dir}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
