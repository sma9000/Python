# Author: <Salma Awan>
# Implementation of BlackJack Game

import random

FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16


####### DO NOT EDIT ABOVE ########
def deal_card():
    # helps choose a random card within the range of of the CARD_LABELS and returns card value
    cardval = random.choice(CARD_LABELS)
    return cardval


def get_card_value(card_label):
    # evaluates integer value to card label
    if card_label.isdigit():
        card_lab = int(card_label)
    else:
        if card_label == 'A':
            card_lab = ACE_VALUE
        else:
            card_lab = FACE_CARD_VALUE
    return card_lab


def deal_cards_to_player():
    # deals card to player and returns the total
    card = deal_card()
    facecard = get_card_value(card)

    card2 = deal_card()
    facecard2 = get_card_value(card2)

    total = facecard + facecard2
    print('Player drew', card, 'and', card2+'.')
    print("Player's total is", str(total)+'.\n')
    q = input('Hit (h) or Stay (s)?')
    print('')
    while q != 's':
        if q == 'h':
            card3 = deal_card()
            facecard3 = get_card_value(card3)
            total += facecard3
            print('Player drew', card3)
            print("Player's total is", str(total)+'.\n')
        if total >= BLACKJACK:
            return total
        q = input('Hit (h) or Stay (s)?')
        print('')
    return total

def deals_cards_to_dealer():
    # deals cards to dealer and returns the total
    card = deal_card()
    facecard = get_card_value(card)

    card2 = deal_card()
    facecard2 = get_card_value(card2)

    total = facecard + facecard2

    print('Dealer drew', card, 'and', card2+'.')
    print("Dealer's total is", str(total)+'.\n')

    while total < DEALER_THRESHOLD:
        card3 = deal_card()
        facecard3 = get_card_value(card3)
        total += facecard3
        print('Dealer drew', card3)
        print("Dealer's total is", str(total)+'.\n')

    return total


def determine_outcome(player_total, dealer_total):
    # determines outcome of game and the value of cards received by the player and the dealer
    if player_total > BLACKJACK:
        print('YOU LOSE!\n')
    elif player_total == BLACKJACK:
        if dealer_total == BLACKJACK:
            print('YOU LOSE!\n')
        else:
            print('YOU WIN!\n')
    else:
        if dealer_total <= BLACKJACK and dealer_total < player_total:
            print('YOU WIN!\n')
        elif dealer_total > BLACKJACK:
            print('YOU WIN!\n')
        elif dealer_total >= player_total:
            print('YOU LOSE!\n')


def play_blackjack():
    # allows user to play Blackjack
    print("Let's Play Blackjack!")
    pc = deal_cards_to_player()
    dc = deals_cards_to_dealer()
    determine_outcome(pc, dc)
    play_again = input('Play again (Y/N)?')
    while play_again != 'N':
        if play_again == 'Y':
            pc = deal_cards_to_player()
            dc = deals_cards_to_dealer()
            determine_outcome(pc, dc)
        play_again = input('Play again(Y/N?')
    print('')
    print('Goodbye.')


def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """

    # call play_blackjack() here and remove pass below
    play_blackjack()


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()
