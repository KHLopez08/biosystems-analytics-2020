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
    
    if len(args.players) > 4:
        parser.error(f' "{args.players}" are too much players, there must be 4 players or less.')

    return args

# --------------------------------------------------
def create_deck():
    face_of_card = []
    suit_of_card = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    royal_cards = ['11', '12', '13', '14']
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

    for k in range(0, 52):
            i = random.randint(0, 51)
            j = random.randint(0, 51)
                      
            temp = deck_of_cards[i]
            deck_of_cards[i] = deck_of_cards[j]
            deck_of_cards[j] = temp
          
    random.shuffle(deck_of_cards)
    return deck_of_cards


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    random.seed(args.seed)
    participants = args.players
    list_of_player = {participants[i]: args.money for i in range(len(participants))}
    bank = {'Bank': args.bank}
    deck = create_deck()
    deck_shuffled = shuffle_cards(deck)


    for m in range(len(deck_shuffled)):
        while int(bank.get('Bank')) > 0:
            if len(deck_shuffled) < 10:
                deck = create_deck()
                deck_shuffled = shuffle_cards(deck)

            for n in range(len(participants)):

                if int(bank.get('Bank')) <= 0:
                    break

                if int(list_of_player[participants[n]]) <= 0:
                    print(f'Oooooooooh no!!! {participants[n]} does not have money and is out of the game')
                    continue
                else:
                    card1 = deck_shuffled.pop()
                    card2 = deck_shuffled.pop()
                    card3 = deck_shuffled.pop()
                    rndm_card = deck_shuffled.pop()
                    article1 = 'an' if int(card1[0:2]) in (8, 11) else 'a'
                    article2 = 'an' if int(card2[0:2]) in (8, 11) else 'a'
                    article3 = 'an' if int(card3[0:2]) in (8, 11) else 'a'
                    print(bank)
                    print(list_of_player, end='\n')
                    print(
                        f'{participants[n]} your card is {article1} "{card1}" and the dealer\'s card is {article2} "{card2}".')
                    change_card = input('Would you like to change or keep your card? (Type change to "change"  or any key to "keep"): ')
                    if change_card.lower() == 'change':
                        card1 = rndm_card
                        print(f'Your new card is {article1} "{card1}".')
                    bet = int(input('Please, place your bet: '))
                    bet = list_of_player.get(participants[n]) if bet > list_of_player.get(participants[n]) else bet
                    print(f'\nThe dealer places {article3} "{card3}" on the table!')
                    if int(card1[0:2]) == int(card3[0:2]) or int(card2[0:2]) == int(card3[0:2]):
                        print('The third face-up card matches with one of the first two.\nYOU LOSE!!!')
                        print(f'You lose {bet} chips in this round\n')
                        new = list_of_player.get(participants[n]) - bet
                        list_of_player[participants[n]] = new
                    elif int(card1[0:2]) == int(card2[0:2]):
                        print('The two face-up cards are the same.\nYOU WIN!!!')
                        print('You win 1 chip in this round.\n')
                        new = list_of_player.get(participants[n]) + 1
                        list_of_player[participants[n]] = new
                    elif int(card1[0:2]) == int(card2[0:2]) + 1 or int(card1[0:2]) == int(card2[0:2]) - 1:
                        print('The two face-up cards are consecutive.\nYOU LOSE!!!')
                        print(f'You lose {bet} chips in this round.\n')
                        new = list_of_player.get(participants[n]) - bet
                        list_of_player[participants[n]] = new
                    else:
                        if (int(card3[0:2]) > int(card1[0:2]) and int(card3[0:2]) < int(card2[0:2])) or \
                                (int(card3[0:2]) < int(card1[0:2]) and int(card3[0:2]) > int(card2[0:2])):
                            print(f'The third face-up card is between "{card1}" and "{card2}".\nYOU WIN!!!')
                            print(f"You win {bet} chips in this round.\n")
                            bank['Bank'] = bank.get('Bank') - bet
                            new = list_of_player.get(participants[n]) + bet
                            list_of_player[participants[n]] = new
                        else:
                            print(f'The third face-up card is not between "{card1}" and "{card2}".\nYOU LOSE!!!')
                            print(f'You lose {bet} chips in this round.\n')
                            bank['Bank'] = bank.get('Bank') + bet
                            new = list_of_player.get(participants[n]) - bet
                            list_of_player[participants[n]] = new
        else:
            print(f'GAME OVER! \nFinal Scores: {list_of_player}')
            break

        
 
# --------------------------------------------------
if __name__ == '__main__':
    main()
