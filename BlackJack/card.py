import random

def card(cards):
    random_card = random.choice(list(cards.items()))
    cards.pop(random_card[0])
    return random_card

