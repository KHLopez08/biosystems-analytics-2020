#!/usr/bin/env python3
"""
Author : None
Date   : 2020-05-05
Purpose: Count DNA nucleotides
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Count DNA nucleotides',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        metavar='str',
                        help='DNA')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.dna
    a_counter, c_counter, g_counter, t_counter = 0,0,0,0

    for i in range(len(dna)):
        if dna[i].upper() == 'A':
            a_counter += 1
        elif dna[i].upper() == 'C':
            c_counter += 1
        elif dna[i].upper() == 'G':
            g_counter += 1
        elif dna[i].upper() == 'T':
            t_counter += 1

    print(f'{a_counter} {c_counter} {g_counter} {t_counter}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
