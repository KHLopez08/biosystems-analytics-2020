#!/usr/bin/env python3
"""
Author : khlopez08
Date   : 2020-02-13
Purpose: What to do on each day
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='What to do on each day',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('days',
                        metavar='str',
                        nargs='+',
                        help='Days of the week')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    day = args.days
    
    week = {'Monday': 'On Mondays I never go to work',
            'Tuesday': 'On Tuesdays I stay at home',
            'Wednesday': 'On Wednesdays I never feel inclined',
            'Thursday': "On Thursdays, it's a holiday",
            'Friday': 'And Fridays I detest',
            'Saturday': "Oh, it's much too late on a Saturday",
            'Sunday': 'And Sunday is the day of rest'}
    
    
    for char in day:
        print(week.get(char, f'Can\'t find "{char}"'), end='')
        print()
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
