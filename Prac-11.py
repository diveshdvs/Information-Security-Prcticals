def rc4(key, plaintext):
    # Initialize the S and T arrays
    S = [i for i in range(256)]
    T = [ord(key[i % len(key)]) for i in range(256)]
    
    # Initialize the index variables
    i, j = 0, 0
    
    # Generate the pseudorandom stream of bytes
    for k in range(256):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        
    # Generate the ciphertext by combining the plaintext with the pseudorandom stream using bitwise XOR
    ciphertext = ""
    for k in range(len(plaintext)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        ciphertext += chr(ord(plaintext[k]) ^ S[t])
    
    # Return the ciphertext
    return ciphertext

key = "SECRET_KEY"
plaintext = "HELLO WORLD"
ciphertext = rc4(key, plaintext)
print(ciphertext)
 
