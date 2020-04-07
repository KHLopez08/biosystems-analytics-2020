#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-07
Purpose: Telephone
"""

import argparse
import os
import sys
import random
import string



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)


    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be 0 and 1')
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    alpha = string.ascii_letters + string.punctuation
    
    # new_text = []
    # for char in args.text:
    #     new_char = random.choice(alpha.replace(char, '')) if random.random() <= args.mutations else char
    #     new_text.append(new_char)

    text = args.text
    text_len = len(text)
    num_mutations = round(text_len * args.mutations)
    indexes = random.sample(range(text_len), k=num_mutations)

    new_text = list(text)
    for i in indexes:
        char = text[i]
        new_char = random.choice(alpha.replace(char, ''))
        #print(f'{i:3}: {char} -> {new_char}')
        #new_text = new_text[:i] + new_char + new_text[i+1:]
        new_text[i] = new_char

    print(f'You said: "{args.text}"')
    print('I heard : "{}"'.format(''.join(new_text)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
