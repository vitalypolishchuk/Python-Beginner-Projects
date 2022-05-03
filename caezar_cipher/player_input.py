def player_input():
    while True:
        print('Would you like to (e)ncrypt or (d)ecrypt the message?')
        ed = input('> ')

        if ed[0].lower() == 'e':
            break
        elif ed[0].lower() == 'd':
            break
        else:
            print("Wrong input! Please enter 'e' for encryption or 'd' for decryption")

    while True:
        try:
            print('Please enter a key (1-26)')
            key = int(input('> '))
        except ValueError: # if type(key) != int, then we catch ValueError
            print('Wrong Input! Please enter a number from 1 to 26')
        else:
            if 0 < key < 26:
                break
            else:
                print('Number should be from 1 to 26!')
    
    if ed[0].lower() == 'e':
        translation = 'encrypt'
    else:
        translation = 'decrypt'
    while True:
        print(f'Enter the message to {translation}')
        msg = input('> ')
        return translation, key, msg