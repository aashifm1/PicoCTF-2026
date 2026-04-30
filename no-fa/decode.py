import zlib
import base64

# load up the latest cookie you get from the website after you login
cookie_data = "your-cookie-paste-here"

# decoding with base64 and decompress with zlib
decoded = base64.urlsafe_b64decode(cookie_data + "==")
decompressed = zlib.decompress(decoded)

# print the final result (otp)
print(decompressed.decode())
