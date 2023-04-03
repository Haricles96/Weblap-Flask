from flask_wtf import FlaskForm
from wtforms import StringField,InteregField,SubmitField
from wtforms.validators import DataRequired,Length

class Rendeles_ürlap(FlaskForm):
    email = StringField('E-mail*', validators=[DataRequired(),Length(min=1)])
    vnev = StringField("Vezetéknév*",validators=[DataRequired(),Length(min=1)])
    knev = StringField("Keresztnév*", validators=[DataRequired(),Length(min=1)])
    tel = InteregField("Telefonszám*",validators=[DataRequired(),Length(min=1,max=11)])
    irsz = InteregField("Irányítószám*",validators=[DataRequired(),Length(min=1,max=5)])
    utca = StringField("Utca",validators=[DataRequired(),Length(min=1,max=50)])
    hszam = InteregField("Házszám",validator=[DataRequired(),Length(min=1,max=6)])
    submit = SubmitField("Rendelés")


