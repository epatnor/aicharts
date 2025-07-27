# scraper.py

import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def timestamp():
    return datetime.utcnow().isoformat()

# ========== LIVE SCRAPER: LLM Arena ==========

# scraper.py (only the LLM part updated)

def scrape_llm_arena():
    try:
        url = "https://arena.lmsys.org/"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # New structure: top models are inside .leaderboard-container table rows
        rows = soup.select("table tbody tr")
        if not rows:
            raise ValueError("No table rows found")

        models, scores = [], []
        for row in rows[:5]:
            cols = row.find_all("td")
            if len(cols) >= 3:
                name = cols[1].get_text(strip=True)
                score = float(cols[2].get_text(strip=True))
                models.append(name)
                scores.append(score)

        return {"models": models, "scores": scores, "timestamp": timestamp()}
    except Exception as e:
        print(f"⚠️ Failed to scrape LLM Arena: {e}")
        return fallback_llm()


# ========== MOCK FALLBACKS FOR OTHER CATEGORIES ==========

def fallback_llm():
    return {
        "models": ["GPT-4o", "Claude 3.5", "Gemini 1.5", "DeepSeek", "Command R+"],
        "scores": [95.1, 93.6, 91.3, 89.0, 87.2],
        "timestamp": timestamp()
    }

def scrape_gpqa():
    return {
        "models": ["Gemini 2.5", "GPT-4o", "Claude Opus", "Yi-1.5", "Mistral-MoE"],
        "scores": [21.6, 20.3, 10.7, 9.8, 7.9],
        "timestamp": timestamp()
    }

def scrape_livecode():
    return {
        "models": ["Claude Opus", "o1-mini", "Grok 4", "GPT-4 Turbo", "StarCoder2"],
        "scores": [88.2, 84.2, 81.9, 80.5, 77.0],
        "timestamp": timestamp()
    }

def scrape_bfcl():
    return {
        "models": ["GPT-4-Opus", "Claude 3 Opus", "Command R+", "Yi-1.5", "Grok 1.5"],
        "scores": [92.1, 89.5, 85.4, 83.2, 81.0],
        "timestamp": timestamp()
    }

# ========== WRITE TO FILE ==========

def save_json(filename, data):
    path = os.path.join(DATA_DIR, f"{filename}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved {filename}.json")

if __name__ == "__main__":
    save_json("llm", scrape_llm_arena())
    save_json("gpqa", scrape_gpqa())
    save_json("livecode", scrape_livecode())
    save_json("bfcl", scrape_bfcl())
