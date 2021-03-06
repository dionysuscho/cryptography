# ----- Caeser Cipher v01 ----- #

def encrypt(plaintext: str, key: int) -> str:
    '''
    Using the Ceaser Cipher method to shift the alpha characters of the string 
    plaintext in lowercase by the key amount, then return the encrypted string.
    '''

    ciphertext = ''    
    
    for ch in plaintext: 
        if ch.isalpha():
            num = ord(ch.lower())
            ciphertext += chr((num - 97 + key) % 26 + 97)
        else:
            ciphertext += ch
    
    return ciphertext

while True: 
    plaintext = str(input('Enter your message: '))
    
    key = input('Enter an integer key: ')
    
    while not ((key[0] == '-' and key[1: ].isdigit()) or key.isdigit()):
        key = input('Enter an integer key: ')
    
    key = int(key)

    print ('\n' + encrypt(plaintext, key) + '\n')