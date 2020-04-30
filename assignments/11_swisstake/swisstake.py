#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-29
Purpose: Filter SwissProt file for keywords, taxa
"""

import argparse
import os
import sys
import random
from Bio import SeqIO
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter SwissProt file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='SwissProt file')

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='keyword',
                        type=str,
                        nargs = '+',
                        default= None,
                        required= True)
    
    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        metavar='taxa',
                        nargs = '*',
                        type=str,
                        default= None)
    
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type= argparse.FileType('wt'),
                        default='out.fa')

    args = parser.parse_args()
        
    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    skip = set(map(str.lower, args.skiptaxa or []))
    input_keyword = set(map(str.lower, args.keyword))
    skip_count = 0
    keyword_count = 0
    

    for rec in SeqIO.parse(args.file, 'swiss'):

        taxa = rec.annotations.get('taxonomy')
        if taxa:
            taxa = set(map(str.lower, taxa))
            if skip.intersection(taxa):
                skip_count += 1
                continue

        keywords = rec.annotations.get('keywords')
        if keywords:
            keywords = set(map(str.lower, keywords))
            if input_keyword.intersection(keywords):
                keyword_count += 1
                SeqIO.write(rec, args.outfile, 'fasta-2line')
        
    
    print(f'Done, skipped {skip_count} and took {keyword_count}. See output in "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
