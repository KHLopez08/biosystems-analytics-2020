#!/usr/bin/env python3
"""
Author : khlopez08
Date   : 2020-02-11
Purpose: Favorite Things
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Favorite Things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('favorite',
                        metavar='str',
                        nargs='+',
                        help='My favorite things')

    parser.add_argument('-s',
                        '--sep',
                        metavar='str',
                        type = str,
                        default = ', ',
                        help='Change comma for sepparator')

    
#    parser.add_argument('-s',
#                        '--sep',
#                        action='store_true',
#                        help='Separate the items with a separator')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    things = args.favorite
    num = len(things)
    separator = args.sep
    
    like = ''
    
    if num == 1:
        like = things[0]
        print(f'{like}')
        print('This is one of my favorite things.')
    else:
        like = separator.join(things)
        print(f'{like}')
        print('These are a few of my favorite things.')
    
    
    
#    print(f'{things}')
#    print('This is one of my favorite things')


        
    
    
    
    
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
