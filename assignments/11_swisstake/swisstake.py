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
                        help='SwissProt file')

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='keyword',
                        nargs = '+',
                        type=str,
                        default= None,
                        required= True)
    
    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        metavar='taxa',
                        nargs = '+',
                        type=str,
                        default= None)
    
    parser.add_argument('-o',
                        '--output',
                        help='Output filename',
                        metavar='FILE',
                        type= argparse.FileType('wt'),
                        default='out.fa')

    args = parser.parse_args()
    
    if os.path.isfile(args.file):
        args.file = open(args.file).read().rstrip()
        
    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    skip_count = 0
    keyword_count = 0
    # parser = SeqIO.parse(args.file, 'swiss')
    # rec = list(parser)[0]
    # print(rec)
    for rec in SeqIO.parse(args.file, 'swiss'):
        taxa = set(map(str.lower, taxonomy))
        keyword = set(map(str.lower, keywords))
        skip = set(map(str.lower, args.skiptaxa))
        input_keyword = set(map(str.lower, args.keyword))
        
        for rec.annotation in rec:
            if skip.intersection(taxa) == True:
                skip_count += 1
                continue
            
            elif input_keyword.intersection(keyword) == True:
                keyword_count += 1
                SeqIO.write(rec, args.outfile, 'fasta')
    
    print(f'Done, skipped {skip_count} and took {keyword_count}. See output in {args.output.name}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
