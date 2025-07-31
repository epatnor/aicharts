# server.py

from flask import Flask, jsonify, render_template
import os
import json

# 🔧 Kontrollera var scriptet körs ifrån
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

# 🚀 Flask-app med rätt paths
app = Flask(__name__,
            template_folder=TEMPLATE_DIR,
            static_folder=STATIC_DIR,
            static_url_path='/static')

# 🔎 Läs JSON-data från /data
def load_json(name):
    path = os.path.join(DATA_DIR, f"{name}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"error": "Data not found"}

# 🔌 API-endpoints
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

# 🧪 Kontrollera att index.html hittas
@app.route("/")
def dashboard():
    test_path = os.path.join(TEMPLATE_DIR, "index.html")
    if not os.path.exists(test_path):
        return f"❌ Hittar inte {test_path}", 500
    return render_template("index.html")

# ▶️ Kör appen
if __name__ == "__main__":
    print(f"✅ Körs från: {BASE_DIR}")
    print(f"📁 Templates: {TEMPLATE_DIR}")
    print(f"📁 Static:    {STATIC_DIR}")
    app.run(debug=True, port=8000)
