from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nombre = "Usuario"
    enlaces = [
        {'nombre': 'Sección 1', 'url': 'https://www.ejemplo.com/seccion1'},
        {'nombre': 'Sección 2', 'url': 'https://www.ejemplo.com/seccion2'},
        {'nombre': 'Sección 3', 'url': 'https://www.ejemplo.com/seccion3'}
    ]
    return render_template('index.html', nombre=nombre, enlaces=enlaces)

if __name__ == '__main__':
    app.run(debug=True)
