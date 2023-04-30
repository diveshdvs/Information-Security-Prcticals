def generate_playfair_table(key):
    table = []
    key = key.replace("J", "I").upper()
    for letter in key:
        if letter not in table and letter.isalpha():
            table.append(letter)
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letter not in table:
            table.append(letter)
    return table

def playfair_cipher(plaintext, key):
    table = generate_playfair_table(key)
    plaintext_pairs = []
    plaintext = plaintext.replace("J", "I").upper()
    plaintext = "".join([c for c in plaintext if c.isalpha()])
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i+1]:
            plaintext_pairs.append(plaintext[i] + "X")
            i += 1
        else:
            plaintext_pairs.append(plaintext[i:i+2])
            i += 2
    ciphertext_pairs = []
    for pair in plaintext_pairs:
        row1, col1 = divmod(table.index(pair[0]), 5)
        row2, col2 = divmod(table.index(pair[1]), 5)
        if row1 == row2:
            ciphertext_pairs.append(table[row1*5+(col1+1)%5] + table[row2*5+(col2+1)%5])
        elif col1 == col2:
            ciphertext_pairs.append(table[((row1+1)%5)*5+col1] + table[((row2+1)%5)*5+col2])
        else:
            ciphertext_pairs.append(table[row1*5+col2] + table[row2*5+col1])
    ciphertext = "".join(ciphertext_pairs)
    return ciphertext
plaintext = "hello world"
key = "prerna"
ciphertext = playfair_cipher(plaintext, key)
print(ciphertext)
