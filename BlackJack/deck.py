import random

def deck():
    """Return a list of (rank, suit) tuples for all 52 cards."""

    royal_ranks = ['J','Q','K','A']
    # Character 9829 is '♥' Character 9830 is '♦' 
    # Character 9824 is '♠' Character 9827 is '♣'
    suits = [chr(9829), chr(9830), chr(9824), chr(9827)] 
    deck = []

    for suit in suits:
        for rank in range(1,11):
            deck.append((str(rank),suit))
    for suit in suits:
        for rank in ['J','Q','K','A']:
            deck.append((str(rank),suit))
    random.shuffle(deck)
    return deck