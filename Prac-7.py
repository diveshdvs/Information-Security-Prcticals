def rail_fence_cipher(plaintext, rails):
    cipher_rails = [""] * rails
    direction = 1    
    rail = 0
    for c in plaintext:
        cipher_rails[rail] += c
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
        ciphertext = "".join(cipher_rails)
    return ciphertext
plaintext = "HELLO WORLD"
rails = 3
ciphertext = rail_fence_cipher(plaintext, rails)
print(ciphertext)
