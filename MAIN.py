import psycopg2
from flask import Flask, redirect, render_template, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
import db
from forms import LibrosForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'SUPER SECRETO'

@app.route('/')
def index():
    return render_template('base.html')

@app.errorhandler(404)
def error404(error):
    return render_template('404.html')



@app.route('/libro')
def libros():
    conn = db.conectar()
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    # Ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM libros_view''')
    # Recuperar la información
    datos = cursor.fetchall()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('libro.html', datos=datos)

@app.route('/insertar_libro', methods=['GET', 'POST'])
def insertar_libro():
    form = LibrosForm()
    if form.validate_on_submit():
        titulo = form.titulo.data
        fk_autor = form.fk_autor.data
        fk_editorial = form.fk_editirial.data
        edicion = form.edicion.data
        conn = db.conectar()
        cursor = conn.cursor()
        cursor.execute(''' INSERT INTO libro ( titulo, fk_autor, fk_editorial, edicion)
                       VALUES (%s,%s,%s,%s)
        ''',(titulo, fk_autor, fk_editorial, edicion ))
        conn.commit()
        cursor.close()
        db.desconectar()
        return redirect(url_for('libros'))
    
    return render_template('insertar_libro.html', form=form)

@app.route('/autores')
def autores():
    conn = db.conectar()
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    # Ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM autores_view''')
    # Recuperar la información
    datos = cursor.fetchall()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('autores.html', datos=datos)

@app.route('/paises')
def paises():
    conn = db.conectar()
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM pais ORDER BY id_pais''')
    # Recuperar la información
    datos = cursor.fetchall()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('paises.html', datos=datos)

@app.route('/delete_pais/<int:id_pais>', methods=['POST'])
def delete_pais(id_pais):
    conn = db.conectar()
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    # crear un cursor (objeto para recorrer las tablas)
    # Borrar el registro con el id_pais seleccionado
    cursor.execute('''DELETE FROM pais WHERE id_pais=%s''',
                   (id_pais,))
    conn.commit()
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for('index'))

@app.route('/update1_pais/<int:id_pais>', methods=['POST'])
def update1_pais(id_pais):
    conn = db.conectar()
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    # recuperar el registro del id_pais seleccionado
    cursor.execute('''SELECT * FROM pais WHERE id_pais=%s''',
                   (id_pais,))
    datos = cursor.fetchall()
    cursor.close()
    db.desconectar(conn)
    return render_template('editar_pais.html', datos=datos)

@app.route('/update2_pais/<int:id_pais>', methods=['POST'])
def update2_pais(id_pais):
    nombre = request.form['nombre']
    conn = db.conectar()
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    cursor.execute('''UPDATE pais SET nombre=%s WHERE id_pais=%s''', (nombre, id_pais,))
    conn.commit()
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for('index'))