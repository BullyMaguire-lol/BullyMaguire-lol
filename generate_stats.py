import requests
import json
from datetime import datetime

USERNAME = "BullyMaguire-lol"

url = f"https://api.github.com/users/{USERNAME}"
data = requests.get(url).json()

repos = data.get("public_repos", 0)
followers = data.get("followers", 0)
following = data.get("following", 0)

svg = f"""
<svg width="450" height="180" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0f172a"/>
  <text x="20" y="40" fill="#38bdf8" font-size="22" font-family="monospace">
    GitHub Stats — {USERNAME}
  </text>

  <text x="20" y="80" fill="#e5e7eb" font-size="16" font-family="monospace">
    📦 Public Repos: {repos}
  </text>

  <text x="20" y="110" fill="#e5e7eb" font-size="16" font-family="monospace">
    👥 Followers: {followers}
  </text>

  <text x="20" y="140" fill="#e5e7eb" font-size="16" font-family="monospace">
    🔗 Following: {following}
  </text>

  <text x="20" y="165" fill="#6b7280" font-size="12" font-family="monospace">
    Updated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}
  </text>
</svg>
"""

with open("assets_stats.svg", "w") as f:
    f.write(svg)
