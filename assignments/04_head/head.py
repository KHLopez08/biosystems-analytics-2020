#!/usr/bin/env python3
"""
Author : khlopez08
Date   : 2020-02-20
Purpose: Read a file
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Read a file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    
    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Name of the file')

    parser.add_argument('-n',
                        '--num',
                        help='Number of lines to be read',
                        metavar='int',
                        type=int,
                        default= 10)

    args = parser.parse_args()
    
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
        
    return args


# --------------------------------------------------
def main():
    """The Imperial March sounds"""

    args = get_args()
    
    for i in range(args.num):
        if args.num >= 1:
            for fh in args.file:
                print(fh.readline(), end='')
        

# --------------------------------------------------
if __name__ == '__main__':
    main()
