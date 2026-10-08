import os
import pickle
from flask import Flask, request

app = Flask(__name__)

SECRET_KEY = "admin123"  # hardcoded secret

@app.route("/ping")
def ping():
    host = request.args.get("host")
    subprocess.run(["ping", "-c", "1", host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return "done"

@app.route("/calc")
def calc():
    expr = request.args.get("expr")
    return str(eval(expr))  # arbitrary code execution

@app.route("/load", methods=["POST"])
def load():
    data = pickle.loads(request.data)  # insecure deserialization
    return str(data)

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1")
