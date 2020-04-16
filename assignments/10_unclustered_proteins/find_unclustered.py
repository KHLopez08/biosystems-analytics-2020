#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-14
Purpose: Find proteins not clustered by CD-HIT
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
        description='Find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c',
                        '--cdhit',
                        help='Output file from CD-HIT (clustered proteins)',
                        metavar='cdhit',
                        type=argparse.FileType('r'),
                        required= True,
                        default=None)
    
    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='proteins',
                        type=argparse.FileType('r'),
                        required= True,
                        default=None)
    
    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default='unclustered.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    cluster_ids = set()
    protein_ids = set()
    num_sequence = 0

    for line in args.cdhit:
        if line[0] == '>':
            continue
        else:
            match = re.search(r'>(\d+)', line)
            id = match.group(1)
            cluster_ids.add(id)
    
    total_proteins = len(cluster_ids)
    #print(total_proteins)

    for rec in SeqIO.parse(args.proteins, 'fasta'):
        p_id = rec.id
        new_id = re.sub(r'\|.*', '', p_id)
        protein_ids.add(new_id)
        if protein_ids not in cluster_ids:
            SeqIO.write(rec, args.outfile, 'fasta')
            num_sequence += 1
    
    #print(len(protein_ids))


    print(f'Wrote {num_sequence} of {total_proteins} unclustered proteins to "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()