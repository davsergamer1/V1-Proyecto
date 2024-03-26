from flask import Flask, render_template, redirect, url_for, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import pandas as pd
from openpyxl import load_workbook

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'  # Cambia esto por una clave segura

usuarios_registrados_file = 'usuarios_registrados.xlsx'  # Nombre del archivo Excel

# Crea un archivo Excel si no existe y agrega una hoja de datos
try:
    pd.read_excel(usuarios_registrados_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=['nombre_usuario', 'correo', 'contraseña'])
    df.to_excel(usuarios_registrados_file, index=False)

class RegistroForm(FlaskForm):
    nombre_usuario = StringField('Nombre de Usuario')
    correo = StringField('Correo Electrónico')
    contraseña = PasswordField('Contraseña')
    enviar = SubmitField('Registrarse')

@app.route('/')
def index():
    nombre_usuario = session.get('nombre_usuario', None)
    return render_template('index.html', nombre_usuario=nombre_usuario)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()

    if form.validate_on_submit():
        nombre_usuario = form.nombre_usuario.data
        correo = form.correo.data
        contraseña = form.contraseña.data

        # Agrega el nuevo usuario al archivo Excel
        df = pd.read_excel(usuarios_registrados_file)
        nuevo_usuario = pd.DataFrame({'nombre_usuario': [nombre_usuario], 'correo': [correo], 'contraseña': [contraseña]})
        df = pd.concat([df, nuevo_usuario], ignore_index=True)
        df.to_excel(usuarios_registrados_file, index=False)

        session['nombre_usuario'] = nombre_usuario
        return redirect(url_for('index'))

    return render_template('registro.html', form=form)

@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.pop('nombre_usuario', None)
    return redirect(url_for('index'))

@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    error = None

    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        contraseña = request.form['contraseña']

        # Verifica si el usuario y la contraseña coinciden (simulado)
        df = pd.read_excel(usuarios_registrados_file)
        usuario = df[(df['nombre_usuario'] == nombre_usuario) & (df['contraseña'] == contraseña)]

        if not usuario.empty:
            session['nombre_usuario'] = nombre_usuario
            return redirect(url_for('index'))
        else:
            error = 'Usuario o contraseña incorrecta'

    return render_template('iniciar_sesion.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)