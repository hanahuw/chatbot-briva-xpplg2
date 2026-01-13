from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("briva-xpplg2.json", encoding="utf-8") as f:
    data_siswa = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip().lower()
    kandidat = []

    for siswa in data_siswa:
        if user_message in siswa["nama"].lower():
            kandidat.append(siswa)

    if len(kandidat) == 1:
        return jsonify({
            "type": "success",
            "nama": kandidat[0]["nama"],
            "briva": kandidat[0]["briva"]
        })
    elif len(kandidat) > 1:
        return jsonify({
            "type": "error",
            "message": "Nama ditemukan lebih dari satu. Silakan tulis nama lebih lengkap."
        })
    else:
        return jsonify({
            "type": "error",
            "message": "Data siswa tidak ditemukan."
        })

if __name__ == "__main__":
    app.run(debug=True)
