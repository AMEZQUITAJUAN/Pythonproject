from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return '<h1>¿Quieres saber quien es realmente jua jose?</h1>'

@app.route('/adivina/')
@app.route('/adivina/<nombre>')
def saluda(nombre=None):
    return render_template("index.html",nombre=nombre)