def caesar_cipher(text, key):
    text = text.upper()
    ciphertext = ""
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - 65 + key) % 26
            ciphertext += chr(shifted + 65)
        else:
            ciphertext += char
    return ciphertext
def rail_fence_cipher(text, key):
    fence = [['\n' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0
    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        fence[row][col] = char
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    ciphertext = ""
    for i in range(key):
        for j in range(len(text)):
            if fence[i][j] != '\n':
                ciphertext += fence[i][j]
    return ciphertext

def product_cipher(plaintext, caesar_key, rail_fence_key):
    caesar_ciphertext = caesar_cipher(plaintext, caesar_key)
    rail_fence_ciphertext = rail_fence_cipher(caesar_ciphertext, rail_fence_key)
    return rail_fence_ciphertext

plaintext = "HELLO WORLD"
caesar_key = 3
rail_fence_key = 3
ciphertext = product_cipher(plaintext, caesar_key, rail_fence_key)
print(ciphertext)

