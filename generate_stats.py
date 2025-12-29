import requests
from datetime import datetime

USERNAME = "BullyMaguire-lol"

url = f"https://api.github.com/users/{USERNAME}"
response = requests.get(url)

# Handle API problems safely
if response.status_code != 200:
    data = {}
else:
    data = response.json()

public_repos = data.get("public_repos", 0)
followers = data.get("followers", 0)
following = data.get("following", 0)

updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

svg = f"""
<svg width="460" height="190" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" rx="14" ry="14" fill="#0f172a" />

  <text x="22" y="38" fill="#38bdf8" font-size="22" font-family="monospace">
    GitHub Stats — {USERNAME}
  </text>

  <text x="22" y="82" fill="#e5e7eb" font-size="16" font-family="monospace">
    📦 Public Repos: {public_repos}
  </text>

  <text x="22" y="112" fill="#e5e7eb" font-size="16" font-family="monospace">
    👥 Followers: {followers}
  </text>

  <text x="22" y="142" fill="#e5e7eb" font-size="16" font-family="monospace">
    🔗 Following: {following}
  </text>

  <text x="22" y="172" fill="#9ca3af" font-size="12" font-family="monospace">
    Updated: {updated}
  </text>
</svg>
"""

with open("assets_stats.svg", "w", encoding="utf-8") as f:
    f.write(svg)
