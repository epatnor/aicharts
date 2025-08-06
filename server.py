# server.py
# Flask-server för AICharts med disciplin‑specifika API‑endpoints

from flask import Flask, jsonify, render_template
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

# skapa app med rätt template och static paths
app = Flask(__name__,
            template_folder=TEMPLATE_DIR,
            static_folder=STATIC_DIR,
            static_url_path='/static')

def load_json(name):
    # läser fil name.json från data/ om den finns, annars returnerar error
    path = os.path.join(DATA_DIR, f"{name}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf‑8") as f:
            return json.load(f)
    return {"error": "Data not found"}

# befintliga API-rutter
@app.route("/api/llm")
def llm():
    return jsonify(load_json("llm"))

@app.route("/api/reasoning")
def reasoning():
    return jsonify(load_json("reasoning"))

@app.route("/api/coding")
def coding():
    return jsonify(load_json("coding"))

@app.route("/api/gpqa")
def gpqa():
    return jsonify(load_json("gpqa"))

@app.route("/api/livecode")
def livecode():
    return jsonify(load_json("livecode"))

@app.route("/api/bfcl")
def bfcl():
    return jsonify(load_json("bfcl"))

# nya API‑endpoints för discipliner från scraper.py
@app.route("/api/general")
def general():
    return jsonify(load_json("general"))

@app.route("/api/math")
def math():
    return jsonify(load_json("math"))

@app.route("/api/tooluse")
def tooluse():
    return jsonify(load_json("tooluse"))

@app.route("/")
def dashboard():
    # kontrollerar att index.html finns och serverar annars felmeddelande
    test_path = os.path.join(TEMPLATE_DIR, "index.html")
    if not os.path.exists(test_path):
        return f"❌ Hittar inte {test_path}", 500
    return render_template("index.html")

if __name__ == "__main__":
    # visa var app körs och vilka mappar som används
    print(f"✅ Körs från: {BASE_DIR}")
    print(f"📁 Templates: {TEMPLATE_DIR}")
    print(f"📁 Static:    {STATIC_DIR}")
    app.run(debug=True, port=8000)
