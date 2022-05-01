from deck import deck
from card import card

class Player:

    def __init__(self,amount):
        self.amount = amount
        self.player_deck = []

    def add_card(self,deck,card):
        self.player_deck.append(card(deck()))
    
    def print_player_deck(self):
        # print_deck = ''
        # for n in range(len(self.player_deck)):
        #     print_deck += self.player_deck[n][0]
        # return print_deck
        return self.player_deck
    
player = Player(100)
print(player.add_card(deck,card))
print(player.add_card(deck,card))
print(player.print_player_deck())