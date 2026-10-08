from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/download")
def download():
    filename = request.args.get("file")
    return send_file("uploads/" + filename)

if __name__ == "__main__":
    app.run()
