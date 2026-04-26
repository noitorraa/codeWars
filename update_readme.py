import requests
from datetime import datetime, timezone

USERNAME = "noitorraa"
CODEWARS_API = f"https://www.codewars.com/api/v1/users/{USERNAME}"


def get_codewars_stats():
    resp = requests.get(CODEWARS_API)
    resp.raise_for_status()
    data = resp.json()
    return {
        "honor": data["honor"],
        "total_completed": data["codeChallenges"]["totalCompleted"],
        "rank": data["ranks"]["overall"]["name"],
        "rank_score": data["ranks"]["overall"]["score"],
        "languages": list(data["ranks"]["languages"].keys())
        if data["ranks"]["languages"]
        else [],
    }


ASCII_BANNER = """
┌─────────────────────────────────────┐
│  > CODEX TERMINAL v2.3              │
│  $ codeWars --user noitorraa        │
│  ██████████████████████████████████ │
└─────────────────────────────────────┘
"""


def generate_readme(stats):
    width = 50
    border = "#" * width
    header = ">> CODYWARS TERMINAL v1.0 <<"
    header_centered = header.center(width)

    terminal_block = f"""
{border}
{header_centered}
{border}

  [>] USER     : {stats["username"]}
  [>] HONOR    : {stats["honor"]}
  [>] RANK     : {stats["rank"]} (score {stats["rank_score"]})
  [>] SOLVED   : {stats["total_completed"]} katas
  [>] LANGUAGES: {", ".join(stats["languages"]).upper() or "—"}

{border}
  LAST UPDATE : {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}
  STATUS      : ONLINE
{border}
"""

    full_content = f"""# CodeWars Stats

<pre>
{ASCII_BANNER.strip()}

{terminal_block.strip()}
</pre>
"""
    return full_content


def main():
    stats = get_codewars_stats()
    stats["username"] = USERNAME
    new_readme = generate_readme(stats)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)


if __name__ == "__main__":
    main()
