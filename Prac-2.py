def checksum(data):
    sum = 0
    for byte in data:
        sum += byte
    return bytes([sum & 0xFF])

data = b'\x01\x02\x03\x04\x05\x06\x07\x08'
expected_checksum = checksum(data)
transmitted_data = data + expected_checksum
received_data = transmitted_data[:-1]
received_checksum = transmitted_data[-1:]
actual_checksum = checksum(received_data)
if expected_checksum == actual_checksum:
    print("No errors detected!")
else:
    print("Error detected in transmission.")

