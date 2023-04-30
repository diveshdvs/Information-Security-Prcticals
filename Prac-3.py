def caesar_cipher(plaintext, shift):
    ciphertext = ""
    for letter in plaintext:
        # Shift the letter by the specified amount
        if letter.isalpha():
            if letter.isupper():
                ciphertext += chr((ord(letter) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(letter) - 97 + shift) % 26 + 97)
        else:
            ciphertext += letter
    return ciphertext

x = caesar_cipher("Ramanujan College",5)
print(x)
