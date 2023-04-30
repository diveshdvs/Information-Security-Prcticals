def row_transposition_cipher(plaintext, key):
    num_cols = len(key)
    padding = (num_cols - len(plaintext) % num_cols) % num_cols
    plaintext += " " * padding
    grid = [list(plaintext[i:i+num_cols]) for i in range(0, len(plaintext), num_cols)]
    sorted_cols = sorted(range(num_cols), key=lambda i: key[i])
    transposed_grid = [[row[i] for i in sorted_cols] for row in grid]
    ciphertext = "".join("".join(row) for row in transposed_grid)
    return ciphertext
plaintext = "HELLO WORLD"
key = "3142"
ciphertext = row_transposition_cipher(plaintext, key)
print(ciphertext)
