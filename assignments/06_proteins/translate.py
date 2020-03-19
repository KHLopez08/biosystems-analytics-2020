#!/usr/bin/env python3
"""
Author : khlopez08
Date   : 2020-03-18
Purpose: Translate DNA/RNA to proteins
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA Sequence')


    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True)
    
    parser.add_argument('-o',
                        '--output',
                        help='Output filename',
                        metavar='FILE',
                        type=str,
                        default='out.txt')
    
    args = parser.parse_args()
        
            
    return args


# --------------------------------------------------
def main():
    """The Imperial March sounds"""

    args = get_args()
    seq = args.sequence
    k = 3
    out_fh= open(args.output, 'wt')   #This line will open the file in args.output for writing a text 

    
    c = {line[:3].upper(): line[4].rstrip() for line in args.codons}    #This will create a dictioanry called "c" by
                                                                        #taking the content of the file in args.codon
    
    for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1, k)]:  #This will separate the argument in groups of 3
        out_fh.write(c.get(codon.upper(), '-'))               #This will write the value of the codon in the output file
    
    print(f'Output written to "{args.output}".')
    out_fh.close()    

# --------------------------------------------------
if __name__ == '__main__':
    main()
