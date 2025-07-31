# server.py

from flask import Flask, jsonify, render_template
import os
import json

# 📁 Skapar Flask-appen
# static_folder: var Flask hittar CSS, JS och bilder
# template_folder: var Flask letar efter HTML-filer som ska renderas
app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static',
    template_folder='templates'
)

# 📂 Mapp där JSON-filer med benchmarkdata sparas
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

# 📄 Läser in en viss JSON-fil från data-mappen
def load_json(name):
    path = os.path.join(DATA_DIR, f"{name}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"error": "Data not found"}

# 📡 API-endpoints – varje funktion returnerar innehållet i motsvarande JSON
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

# 🌐 Huvudsidan – renderar templates/index.html
@app.route("/")
def dashboard():
    return render_template("index.html")

# 🚀 Startar Flask-servern på port 8000
if __name__ == "__main__":
    app.run(debug=False, port=8000)
