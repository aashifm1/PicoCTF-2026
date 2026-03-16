from Crypto.Cipher import AES

state = [0,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,
         0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1]

taps = [63,61,60,58]

bits = []

for _ in range(128):
    bits.append(state[0])

    new_bit = state[63] ^ state[61] ^ state[60] ^ state[58]

    state = state[1:] + [new_bit]

# convert bits → key
key_bytes = []

for i in range(0,128,8):
    byte = bits[i:i+8]
    val = int("".join(str(b) for b in byte),2)
    key_bytes.append(val)

key = bytes(key_bytes)

ciphertext = bytes.fromhex(
"8f0e6d0f5b0dc1db201948b9e0cebd8f4e0f7cb6a86d4243f62f1438e07a632c38338e7e04fbddef0c6260a4eb758417"
)

cipher = AES.new(key, AES.MODE_ECB)

flag = cipher.decrypt(ciphertext)

print(flag)


