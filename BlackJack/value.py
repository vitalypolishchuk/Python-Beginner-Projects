def getHandValue(hand):
    """Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1 (this function picks the most suitable ace value)."""

    value = 0
    numberOfAces = 0

    for card in hand:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ['J','Q','K']:
            value += 10
        else:
            value += int(rank)

    # Add the value for the aces:
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    
    return value
        