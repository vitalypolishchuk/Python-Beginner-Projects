import sys

def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True:
            print(f'How much do you bet? (Max: {maxBet} or QUIT)')
            bet = input('> ')

            if bet[0].lower() == 'q':
                print('Thanks for playing!')
                sys.exit()
            
            if not bet.isdecimal():
                print('Please enter a number!')
                continue

            bet = int(bet)
            if not 1 <= bet <= maxBet:
                print(f'Please enter a number from 1 to {maxBet}')
                continue
            return bet