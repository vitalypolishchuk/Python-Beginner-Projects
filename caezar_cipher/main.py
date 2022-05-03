# The Caesar cipher is an ancient encryption
# algorithm used by Julius Caesar. It
# encrypts letters by shifting them over by a
# certain number of places in the alphabet.

from player_input import player_input
from process import process

def caesar_cipher():
    translation, key, msg = player_input()
    return process(translation,key,msg)

if __name__=='__main__':
    print(caesar_cipher())