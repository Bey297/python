import requests
import random

# Baca file TXT
with open("user_agents.txt", "r") as file:
    user_agents = [
        line.strip()
        for line in file
        if line.strip()
    ]

# Ambil UA secara acak
ua = random.choice(user_agents)

headers = {
    "User-Agent": ua
}

response = requests.get(
    "https://example.com",
    headers=headers
)

print("UA:", ua)
print("Status:", response.status_code)
