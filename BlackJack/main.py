print('''Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.''')

import sys
from bet import getBet
from deck import deck
from hand import displayHands
from hit_or_stand import hit_or_stand
from value import getHandValue
from check_for_winner import check_for_winner

def blackjack(money):
    while True: # Main game loop.
        if money <= 0:
            print('You have lost all your money!')
            sys.exit()
        bet = getBet(money) # ask for bet
        # give two cards to a dealer, but hide first card
        dealerHand = [deck().pop(),deck().pop()]
        # give two cards to a player
        playerHand = [deck().pop(),deck().pop()]

        while True: # Keep looping until player stands or busts.
            # display dealer's hand
            displayHands(playerHand,dealerHand,False)
            # ask player whether he wants to hit or stand
            move = hit_or_stand()
            # if player wants to hit append a card
            if move == True:
                playerHand.append(deck().pop())
                # chech hand's value
                if getHandValue(playerHand) > 21: # player busts
                    break # break out of the game
                else:
                    continue # continue to play
            else: # player wants to stand
                break # break out of the game
        
        if getHandValue(playerHand) > 21:
            displayHands(playerHand,dealerHand,True)
            print('Unfortunately you have lost!')
            money -= bet
        else:
            # if dealer's value < 17, append cards using loop
            while getHandValue(dealerHand) < 17:
                dealerHand.append(deck().pop())

            displayHands(playerHand,dealerHand,True)
            winner = check_for_winner(getHandValue(playerHand),getHandValue(dealerHand)) # check for winner
            
            if winner == True:
                print('Congradulations! You have won the game!')
                money += bet
            elif winner == False:
                print('Unfortunately you have lost!')
                money -= bet
            else:
                print('It is a Tie!')

        if money > 0:
            while True:
                print('Would you like to play again? (Y/N)')
                play_again = input('> ')
                if play_again[0].upper() not in ['Y','N']:
                    continue
                else:
                    break
            if play_again[0].upper() == 'Y':
                continue
            else:
                print('Thanks for playing!')
                sys.exit()
        else:
            sys.exit()

if __name__=='__main__':
    blackjack(100)