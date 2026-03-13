# Read the file
with open('digits.bin', 'r') as f:
    bits = f.read().replace('\n','')  # remove newlines, though your file has none

# Make length multiple of 8
bits = bits[:len(bits) - (len(bits) % 8)]

# Convert to bytes
data = bytearray(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))

# Save as binary
with open('digits_decoded.bin', 'wb') as f:
    f.write(data)
