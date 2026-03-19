
hex_str = "235a201d702015483b1d412b265d3313501f0c072d135f0d2002302d01156a57224306172e"
data = bytes.fromhex(hex_str)

key = b"S3Cr3t"

decoded = ''.join(chr(data[i] ^ key[i % len(key)]) for i in range(len(data)))
print(decoded)
