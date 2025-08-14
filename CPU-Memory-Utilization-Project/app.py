from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stats")
def stats():
    cpu = psutil.cpu_percent(interval=0.4)
    mem = psutil.virtual_memory().percent
    return jsonify(cpu=cpu, memory=mem)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
