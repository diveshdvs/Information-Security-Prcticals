G = [[1, 0, 0, 0, 1, 1, 0],
     [0, 1, 0, 0, 1, 0, 1],
     [0, 0, 1, 0, 0, 1, 1],
     [0, 0, 0, 1, 1, 1, 1]]
# Define the Hamming code parity-check matrix
H = [[1, 1, 0, 1, 1, 0, 0],
     [1, 0, 1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0, 0, 1]]
def hamming_encode(data):
    k = len(data)
    r = 0
    while 2**r < k + r + 1:
        r += 1
    encoded_data = list(data) + [0]*r
    for i in range(r):
        bit = 0
        for j in range(k+r):
            if encoded_data[j] and (j+1) & (1<<i):
                bit ^= 1
        encoded_data[k+i] = bit
    return encoded_data
def hamming_decode(encoded_data):
    n = len(encoded_data)
    r = 0
    while 2**r < n:
        r += 1
    syndrome = []
    for i in range(r):
        bit = 0
        for j in range(n):
            if encoded_data[j] and (j+1) & (1<<i):
                bit ^= 1
        syndrome.append(bit)

    # Correct any errors
    error = 0
    for i in range(r):
        error += syndrome[i] * (1<<i)
    if error:
        encoded_data[error-1] ^= 1

    # Return the decoded data
    return encoded_data[:n-r]

ec = hamming_encode("hello")
dc = hamming_decode(ec)
print(ec,dc)

