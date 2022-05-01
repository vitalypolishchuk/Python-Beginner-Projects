from value import getHandValue
from display_cards import display_cards

def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first"""
    print()
    if showDealerHand:
        print(f'DEALER: {getHandValue(dealerHand)}')
        display_cards(dealerHand)
    else:
        print(f'Dealer: ???')
        display_cards(['backside'] + dealerHand[1:])

    # Show the player's cards:
    print()
    print(f'PLAYER: {getHandValue(playerHand)}')
    display_cards(playerHand)