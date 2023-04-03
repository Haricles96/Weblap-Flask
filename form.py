from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import DataRequired,Length

class Rendeles_ürlap_(FlaskForm):
    email = StringField('E-mail*', validators=[DataRequired(),Length(min=5)])
    vnev = StringField("Vezetéknév*",validators=[DataRequired(),Length(min=2)])
    knev = StringField("Keresztnév*", validators=[DataRequired(),Length(min=2)])
    tel = IntegerField("Telefonszám*",validators=[DataRequired()])
    varos = StringField("Város*",validators=[DataRequired(),Length(min=2,max=30)])
    irsz = IntegerField("Irányítószám*",validators=[DataRequired()])
    utca = StringField("Utca*",validators=[DataRequired(),Length(min=3,max=50)])
    hszam = IntegerField("Házszám*",validators=[DataRequired()])
    submit = SubmitField("Rendelés")


