import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return """
    <h2>Zdravo, kako si?</h2>
    <a href="/odgovor">Idi na odgovor</a>
    """

@app.route("/odgovor")
def hello():
    return """
    <h2>Ja sam odlično, kako si ti?</h2>
    <a href="/app1/">⬅️ Nazad</a>
    """

@app.route("/app1/")
def app1_home():
    return """
    <h2>Dobrodošao na /app1/ stranicu!</h2>
    <a href="/">Idi na početnu</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
