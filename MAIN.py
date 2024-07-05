import psycopg2
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import flaskfrom
wtfforms.fields import passwordfield, stringfield, submitfield

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/libros')
def index():
    #conectar con la base de datos
    Conexion = psycopg2.connect(
        database="biblioteca3A",
        user="postres",
        password="perro12345",
        host="locatlhost",
        port="5432"
    )

    cursor = Conexion.cursor()

    cursor.execute('''SELECT * FROM libros''')

    datos = cursor.fetchall()

    cursor.close()
    Conexion.close()
    return render_template('libros.html', datos)
