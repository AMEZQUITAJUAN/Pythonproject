from flask import Flask

app = Flask(__name__)
@app.route("/")
def hallo_world():
    return "<p>Hola, mundo!!!</p>"