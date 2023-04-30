import numpy as np

def generate_hill_key(n):
    while True:
        key = np.random.randint(26, size=(n, n))
        if np.linalg.det(key) % 26 != 0:
            return key

def hill_cipher(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % key.shape[0] != 0:
        plaintext += "X" * (key.shape[0] - len(plaintext) % key.shape[0])
    plaintext = np.array(list(map(lambda c: ord(c) - ord('A'), plaintext)))
    plaintext = plaintext.reshape(-1, key.shape[0])
    ciphertext = ""
    for col in plaintext.T:
        col = col.reshape(-1, 1)
        encrypted_col = (key @ col) % 26
        ciphertext += "".join(list(map(lambda c: chr(c + ord('A')), encrypted_col.flatten().tolist())))
    
    return ciphertext
plaintext = "HELLO WORLD"
key = generate_hill_key(2)
ciphertext = hill_cipher(plaintext, key)
print(ciphertext)
