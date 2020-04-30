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
    keyword = set()
    taxa = set()
    skip = set(map(str.lower, args.skiptaxa))
    input_keyword = set(map(str.lower, args.keyword))
    skip_count = 0
    keyword_count = 0
    

    for rec in SeqIO.parse(args.file, 'swiss'):
        taxonomy = rec.annotations.get('taxonomy')
        keywords = rec.annotations.get('keywords')
        taxa = set(map(str.lower, taxonomy))
        keyword = set(map(str.lower, keywords))

        if skip.intersection(taxa):
            skip_count += 1
            continue
        
        if input_keyword.intersection(keyword):
            SeqIO.write(rec, args.outfile, 'fasta')
            keyword_count += 1
        
    
    print(f'Done, skipped {skip_count} and took {keyword_count}. See output in "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
