from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Pagina prinsipal'

@app.route('/articulos/')
def articulo():
    return 'Lista de artiulos'

@app.route('/acercade')
def acercade():
    return 'Pagina acerca de...'

@app.route("/articulos/<id>")
def mosttrar_artuculo(id):
    return 'vamos a mostrar el articulo con id{}'.format(id)

@app.route("/hello/")
@app.route("/hello/<string:nombre>")
@app.route("/hello/<string:nombre>/<int:edad>")
def hola(nombre=None, edad=None):
    if nombre and edad:
        return 'Hola, {0} tienes {1} años.'.format(nombre, edad)
    elif nombre:
        return 'Hola, {0}'.format(nombre)
    else:
        return 'Hola mundo'