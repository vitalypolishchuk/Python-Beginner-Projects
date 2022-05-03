import string

def process(translation,key,msg):
    alphabet = string.ascii_uppercase
    encrypted_message = ''

    for letter in msg:
        if letter.upper() in alphabet:
            index = alphabet.index(letter.upper())
            if translation == 'encrypt':
                key_index = (index + key) % len(alphabet) # % - remainder, in case index + key > len(alphabet)
            else:
                key_index = (index - key) % len(alphabet) # % - remainder, in case index - key > len(alphabet)
            encrypted_message += alphabet[key_index]
        else:
            encrypted_message += letter
    return encrypted_message