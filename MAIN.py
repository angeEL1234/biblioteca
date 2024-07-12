import psycopg2
from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/libro')
def libros():
    # Conectar con la base de datos
    conexion = psycopg2.connect(
        database="biblioteca3A",
        user="postgres",
        password="perro12345",
        host="localhost",
        port="5432"
    )
    # crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    # ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM libros_view''')
    #recuperar la informacion
    datos = cursor.fetchall()
    #cerrar cursos y conexion a la base de datos
    cursor.close()
    conexion.close()
    return render_template('libro.html', datos=datos)

@app.route('/autores')
def autores():
    # Conectar con la base de datos
    conexion = psycopg2.connect(
        database="biblioteca3A",
        user="postgres",
        password="perro12345",
        host="localhost",
        port="5432"
    )
    # crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    # ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM autores_view''')
    #recuperar la informacion
    datos = cursor.fetchall()
    #cerrar cursos y conexion a la base de datos
    cursor.close()
    conexion.close()
    return render_template('autores.html', datos=datos)

@app.route('/paises')
def paises():
    # Conectar con la base de datos
    conexion = psycopg2.connect(
        database="biblioteca3A",
        user="postgres",
        password="perro12345",
        host="localhost",
        port="5432"
    )
    # crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    # ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM pais''')
    #recuperar la informacion
    datos = cursor.fetchall()
    #cerrar cursos y conexion a la base de datos
    cursor.close()
    conexion.close()
    return render_template('paises.html', datos=datos)

@app.route('/delete_pais/<int:id_pais>', methods=['POST'])
def delete_pais(id_pais):
    # Tu lógica para eliminar un país
    pass

    # Conectar con la base de datos
    conexion = psycopg2.connect(
        database="biblioteca3A",
        user="postgres",
        password="perro12345",
        host="localhost",
        port="5432"
    )
    # crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()

    cursor.execute('''DELETE FROM pais WHERE id_pais=%s''',
                   (id_pais,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return redirect(url_for('index'))