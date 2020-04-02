#!/usr/bin/env python3
"""
Author : khlopez08
Date   : 2020-04-01
Purpose: Create synthetic sequence
"""

import argparse
import os
import sys
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        metavar= 'str',
                        type = argparse.FileType('wt'),
                        help='Output filename',
                        default= 'out.fa')

    parser.add_argument('-t',
                        '--seqtype',
                        help='DNA or RNA',
                        metavar='str',
                        type=str,
                        choices = ['dna', 'rna'],
                        default= 'dna')

    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default='10')

    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default='50')
                
    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default='75')

    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='float',
                        type=float,
                        default='0.5')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=str,
                        default='None')


    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    # if args.seqtype != 'dna' or args.seqtype != 'rna':
    #     parser.error(f'--seqtype "{args.seqtype}" must be DNA or RNA')

    return args


# --------------------------------------------------

def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases """

    t_or_u = 'T' if seq_type == 'dna' else 'U' 
    num_gc = int((pctgc / 2) * max_len) 
    num_at = int(((1 - pctgc) / 2) * max_len) 
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at 
    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))


# --------------------------------------------------

def test_create_pool():
    """ Test create_pool """

    state = random.getstate() 
    random.seed(1) 
    assert create_pool(.5, 10, 'dna') == 'AAACCCGGTT'
    assert create_pool(.6, 11, 'rna') == 'AACCCCGGGUU'
    assert create_pool(.7, 12, 'dna') == 'ACCCCCGGGGGT'
    assert create_pool(.7, 20, 'rna') == 'AAACCCCCCCGGGGGGGUUU'
    assert create_pool(.4, 15, 'dna') == 'AAAACCCGGGTTTTT'
    random.setstate(state)

# --------------------------------------------------
def main():
    """The Imperial March Sounds"""

    args = get_args()
    random.seed(args.seed)
    sequence_number = 0
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    for _ in range(args.numseqs):
        sequence_number += 1
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = random.sample(pool, k=seq_len)
        print(f'>{sequence_number}', '\n',''.join(seq), file=args.outfile)

    word = 'sequence' if args.numseqs == 1 else 'sequences'
    print(f'Done, wrote {sequence_number} {args.seqtype.upper()} {word} to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
