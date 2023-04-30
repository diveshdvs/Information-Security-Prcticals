def monoalphabetic_cipher(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            if letter.isupper():
                ciphertext += key[ord(letter) - 65]
            else:
                ciphertext += key[ord(letter) - 97].lower()
        else:
            ciphertext += letter
    return ciphertext
plaintext = "hello world"
key = "phqgiumeaylnofdxjkrcvstzwb"
ciphertext = monoalphabetic_cipher(plaintext, key)
print(ciphertext)



def vigenere_cipher(plaintext, key):
    ciphertext = ""
    key_index = 0
    for letter in plaintext:
        if letter.isalpha():
            if letter.isupper():
                shift = ord(key[key_index % len(key)].upper()) - 65
                ciphertext += chr((ord(letter) - 65 + shift) % 26 + 65)
            else:
                shift = ord(key[key_index % len(key)].lower()) - 97
                ciphertext += chr((ord(letter) - 97 + shift) % 26 + 97)
            key_index += 1
        else:
            ciphertext += letter
    return ciphertext
plaintext = "hello world"
key = "lemon"
ciphertext = vigenere_cipher(plaintext, key)
print(ciphertext)
