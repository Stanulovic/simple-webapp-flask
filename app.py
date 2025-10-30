import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Zdravo, kako si?"

@app.route('/odgovor')
def hello():
    return 'Ja sam odlicno, kako si ti?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
