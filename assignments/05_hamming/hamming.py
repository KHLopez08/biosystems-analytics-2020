#!/usr/bin/env python3
"""
Author : khlopez08
Date   : 2020-03-04
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('file',
                        metavar='FILE',
                        default=[sys.stdin],
                        type=argparse.FileType('r'),
                        help='Input file')
    
    
    parser.add_argument('-m',
                        '--min',
                        help='A minimum integer',
                        metavar='int',
                        type=int,
                        default=0)
    
    return parser.parse_args()
# --------------------------------------------------
def main():
    """The Imperial March sounds"""
    
    args = get_args()
    
    for fh in args.file:
        word1, word2 = '', ''
        int1=len(fh.split())
        int2= int1/2
        for i in range(int(int1) - int(int2)):
            for line in fh:
                word1, word2 = fh.split()
                value = [char1 == char2 for char1, char2 in zip(word1, word2)]
                hamming = len(word2) - (sum(value[0:]))

            if hamming >= args.min:
                print(f'{hamming:8}:{word1:20}{word2:20}')
    
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
