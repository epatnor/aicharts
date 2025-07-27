# server.py

from flask import Flask, jsonify, send_from_directory
import os
import json

app = Flask(__name__)
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

# Load a JSON file and return as response
def load_json(name):
    path = os.path.join(DATA_DIR, f"{name}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"error": "Data not found"}

@app.route("/api/gpqa")
def gpqa():
    return jsonify(load_json("gpqa"))

@app.route("/api/livecode")
def livecode():
    return jsonify(load_json("livecode"))

@app.route("/api/bfcl")
def bfcl():
    return jsonify(load_json("bfcl"))

@app.route("/")
def dashboard():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    app.run(debug=False, port=8000)
