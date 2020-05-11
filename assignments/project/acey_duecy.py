#!/usr/bin/env python3
"""
Author : Lia Crocker and K. Humberto Lopez Felix
Date   : 2020-04-20
Purpose: Final Project - plays the card game Acey Duecy
"""

import argparse
import os
import sys
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Play a game of Acey Duecy',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('players',
                        nargs='+',
                        help='Player names text or file',
                        metavar='str',
                        type=str)

    parser.add_argument('-b',
                        '--bank',
                        help='Start value of bank',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--money',
                        help='Start value for players',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-s',
                        '--seed',
                        help='Random Seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    # if os.path.isfile(args.players):
    #     args.players = open(args.players).read().rstrip()
    
    if len(args.players) > 4:
        parser.error(f' "{args.players}" are too much players, there must be 4 players or less.')

    return args

# --------------------------------------------------
def create_deck():
    face_of_card = []
    suit_of_card = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    royal_cards = ['J', 'Q', 'K', 'A']
    deck_of_cards = []

    for i in range(2,11):
        face_of_card.append(str(i))
    for j in range(4):
        face_of_card.append(royal_cards[j])
    for k in range(4):
        for l in range(13):
            card = (face_of_card[l] + " of " + suit_of_card[k])
            deck_of_cards.append(card)
    
    return deck_of_cards
    
# --------------------------------------------------
def shuffle_cards(deck_of_cards):

    random.shuffle(deck_of_cards)

    random_card1 = deck_of_cards.pop(random.randint(0, len(deck_of_cards) -1))
    random_card2 = deck_of_cards.pop(random.randint(0, len(deck_of_cards) -1))
    random_card3 = deck_of_cards.pop(random.randint(0, len(deck_of_cards) -1))
    new_random_card = deck_of_cards.pop(random.randint(0, len(deck_of_cards) -1))

    return random_card1, random_card2, random_card3, new_random_card



# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    participants = args.players
    list_of_player = {participants[i]: args.money for i in range(len(participants))}
    # print(list_of_player)
    value_j = '11'
    value_q = '12'
    value_k = '13'
    value_a = '14'
    high_card = ''
    low_card = ''
    deck = create_deck()
    for m in range(52):
        for n in range(len(participants)):
            random_card1, random_card2, random_card3, new_random_card = shuffle_cards(deck)
            article1 = 'an' if random_card1[0] in('A', '8') else 'a'
            article2 = 'an' if random_card2[0] in('A', '8') else 'a'
            article3 = 'an' if random_card3[0] in('A', '8') else 'a'
            print(f'{participants[n]} your card is {article1} "{random_card1}" and the dealer\'s card is {article2} "{random_card2}".')
            change_card = input('Would you like to change or keep your card? (Type change or keep): ')
            if change_card.lower() == 'change':
                random_card1 = new_random_card
                print(f'Your new card is {article1} "{random_card1}".')
            bet = input('Please, place your bet: ')
            print(f'\nThe dealer places {article3} "{random_card3}" on the table!')
            if random_card1[0] == 'A':
                if value_a > random_card2[0]:
                    high_card = random_card1
                    low_card = random_card2
                else:
                    high_card = random_card2
                    low_card = random_card1
            elif random_card1[0] == 'J':
                if value_j > random_card2[0]:
                    high_card = random_card1
                    low_card = random_card2
                else:
                    high_card = random_card2
                    low_card = random_card1
            elif random_card1[0] == 'Q':
                if value_q > random_card2[0]:
                    high_card = random_card1
                    low_card = random_card2
                else:
                    high_card = random_card2
                    low_card = random_card1
            elif random_card1[0] == 'K':
                if value_k > random_card2[0]:
                    high_card = random_card1
                    low_card = random_card2
                else:
                    high_card = random_card2
                    low_card = random_card1
            elif random_card1[0] > random_card2[0]:
                high_card = random_card1
                low_card = random_card2
            else:
                high_card = random_card2
                low_card = random_card1


            if random_card2[0] == 'A':
                if value_a > random_card2[0]:
                    high_card = random_card1
                    low_card = random_card2
                else:
                    high_card = random_card2
                    low_card = random_card1
            elif random_card2[0] == 'J':
                if value_j > random_card2[0]:
                    high_card = random_card1
                    low_card = random_card2
                else:
                    high_card = random_card2
                    low_card = random_card1
            elif random_card2[0] == 'Q':
                if value_q > random_card2[0]:
                    high_card = random_card1
                    low_card = random_card2
                else:
                    high_card = random_card2
                    low_card = random_card1
            elif random_card2[0] == 'K':
                if value_k > random_card2[0]:
                    high_card = random_card1
                    low_card = random_card2
                else:
                    high_card = random_card2
                    low_card = random_card1
            elif random_card2[0] > random_card1[0]:
                high_card = random_card2
                low_card = random_card1
            else:
                high_card = random_card1
                low_card = random_card2
        #Do comparison for playing card

            # print(random_card1[0])
            print(value_a > random_card2[0])
            print(f'The first card is "{random_card1}" an the second card is "{random_card2}"\n')
            print(f'The higher card is {high_card} and the lower card is {low_card}')
            if random_card3[0] == high_card or random_card3[0] == low_card:
                print('Both cards are equal, you win half pot\n')
            elif random_card3[0] > low_card and random_card3[0] < high_card:
                print('YOU WIN\n')
            else:
                print('Oooooooh, you lose\n')

# --------------------------------------------------
if __name__ == '__main__':
    main()
