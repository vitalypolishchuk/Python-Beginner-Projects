def deck():
    numbers = list(range(1,11))
    royal_cards = ['J','Q','K','A']
    # Character 9829 is '♥' Character 9830 is '♦' 
    # Character 9824 is '♠' Character 9827 is '♣'
    suits = [chr(9829), chr(9830), chr(9824), chr(9827)] 
    deck = {}

    for s in suits:
        for n in numbers:
            if n != 10:
                deck[
f''' ___
|{n}  |   
| {s} |   
|__{n}|
'''
                ] = {n}
            else:
                deck[
f''' ____
|{n}  |   
| {s}  |   
|__{n}|
'''
                ] = {n}
    for s in suits:
        for r in royal_cards:
            if r != 'A':
                deck[
f''' ___
|{r}  |   
| {s} |   
|__{r}|
'''
                ] = 10
            else:
                deck[
f''' ___
|{r}  |   
| {s} |   
|__{r}|
'''] = 11

    return deck

