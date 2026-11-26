import requests
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",

    "Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",

    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1"
]

# Ambil User-Agent secara acak
ua = random.choice(user_agents)

# Masukkan ke headers
headers = {
    "User-Agent": ua
}

# Request
url = "https://example.com"

response = requests.get(url, headers=headers)

print("User-Agent:", ua)
print("Status:", response.status_code)
print(response.text)
