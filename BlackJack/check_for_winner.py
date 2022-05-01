def check_for_winner(player_value,dealer_value):
    if player_value > 21:
        return False
    elif dealer_value > 21:
        return True
    elif player_value > dealer_value:
        return True
    elif dealer_value > player_value:
        return False
    elif player_value == dealer_value:
        return None