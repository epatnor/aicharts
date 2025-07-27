# scraper.py

import json
from datetime import datetime

# Simulated benchmark scraping (replace with real HTML parsing later)
def scrape_gpqa():
    return {"model": "Gemini 2.5 Pro", "score": 21.6, "timestamp": timestamp()}

def scrape_livecode():
    return {"model": "o1-mini", "passAt1": 84.2, "timestamp": timestamp()}

def scrape_bfcl():
    return {"model": "GPT-4-Opus", "accuracy": 92.1, "timestamp": timestamp()}

def timestamp():
    return datetime.utcnow().isoformat()

# Save mock data to disk
def save_json(filename, data):
    with open(f"data/{filename}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    save_json("gpqa", scrape_gpqa())
    save_json("livecode", scrape_livecode())
    save_json("bfcl", scrape_bfcl())
    print("✅ Benchmark data scraped and saved.")
