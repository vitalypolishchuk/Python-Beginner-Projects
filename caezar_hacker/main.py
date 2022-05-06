# This program can hack messages encrypted
# with the Caesar cipher, even
# if you don’t know the key.

import english_words
import re
import string

def caezar_hacker(encrypted_message):
    decrypted_message = []
    alphabet = string.ascii_lowercase # lowercase alphabet, type(str)
    max_index = 0 # count the maximum number of words found in the decrypted message

    encrypted_message_words = re.sub(r'[?!]','',encrypted_message.lower()) # get rid of ?!
    words_list = re.split(r'[,\.]?\s',encrypted_message_words) # turns a string into a list if '.' or ',' or ' ' in the encrypted message
    
    for key in range(26): # Caezar cipher consists only from 26 keys (number of alphabet letters)
        for word in words_list:
            key_word = ''
            for char in word: # go through each character in word to make sure that this character in alphabet
                if char in alphabet:
                    key_index = (alphabet.index(char) - key) % len(alphabet) # the message was initially encrypted by caezar cipher, where given the key (1-26), each letter was moved by that key. For example if the message was 'hi' and key=2, encrypted message would be 'jk' because j goes 2 letters after 'h', and 'k' goes 2 letters after 'i'. So in order to decipher the message, we need to go backwards, take each possible key (1-26) and try corresponding letters from alphabet to see if we can make a word out of this
                    key_word += alphabet[key_index]
            decrypted_message.append(key_word)
        index_count = 0
        for word in decrypted_message:
            for eng_word in list(english_words.english_words_lower_set):
                if len(eng_word) > 1: # we do not need to go through english words that consist from 1 letter
                    if word == eng_word: # if the word from decrypted message was found among eng_words
                        index_count += 1 # count the number of such matches
                        if len(decrypted_message) > 1: # if decrypted message consists of 2+ words, we want to check all of them
                            if index_count > max_index: # count the number of matches in each decrypted message, we will later on return only decrypted message that contains the most matches
                                max_index = index_count # establish the most matches between encrypted message and english words
                                message = decrypted_message
                        else:
                            return ' '.join(decrypted_message) # if decrypted message consists of 1 word and we have a match, stop iteration
        decrypted_message = [] # clear decrypted message, and try next key
    return ' '.join(message)
    
if __name__=='__main__':
    print(caezar_hacker("IGN ID TCRGNEI IWT BTHHPVT XC RPTOPG RXEWTG UXGHI")) 
    