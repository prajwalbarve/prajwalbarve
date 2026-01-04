import requests

USERNAME = "prajwalbarve5557"
url = f"https://tryhackme.com/p/prajwalbarve5557"

data = requests.get(url).json()

content = f"""
## 🔐 TryHackMe Progress (Auto-Updated)

- 🏅 Rank: {data['rank']}
- 🧩 Rooms Completed: {data['rooms_completed']}
- 🎖️ Badges: {len(data['badges'])}
"""

with open("README.md", "w") as f:
    f.write(content)

