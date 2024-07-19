from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class LibrosForm(FlaskForm):
    titulo = StringField('Titulo', validators=[ DataRequired()])
    fk_autor = IntegerField('Autor ID', validators=[ DataRequired()])
    fk_editorial = IntegerField('Editorial', validators=[DataRequired()])
    edicion = IntegerField('edicion', validators=[DataRequired()])
    submit = SubmitField('Agregar libro')