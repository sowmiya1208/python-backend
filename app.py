from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "hello"

@app.route("/health")
def health():
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
