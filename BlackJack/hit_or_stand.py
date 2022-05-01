def hit_or_stand():
    while True:
        print('Would you like to hit or stand? (H/S)')
        move = input('> ')

        if move[0].upper() not in ['H','S']:
            print('Invalid input! Try again!')
            continue
        if move[0].upper() == 'H':
            return True
        return False