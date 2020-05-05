#!/usr/bin/env python3
"""
Author : None
Date   : 2020-05-05
Purpose: Choose the correct Spanish article
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the correct Spanish article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='Input tex')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = ''

    article = 'el' if word[-1] in 'oO' else 'la'
    print(f'Me gusto {article} {word}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
