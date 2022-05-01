def display_cards(cards):
    """Display all the cards in the cards list."""

    row1, row2, row3, row4 = '', '', '', ''
    for card in cards:
        if card == 'backside':
            row1 += ' ___  '
            row2 += '|## | '
            row3 += '|###| '
            row4 += '|_##| '
        else:
            rank,suit = card
            row1 += ' ___  '
            row2 += '|{} | '.format(rank.ljust(2))
            row3 += '| {} | '.format(suit)
            row4 += '|_{}| '.format(rank.rjust(2,'_'))
    print(row1 + '\n' + row2 + '\n' + row3 + '\n' + row4)

