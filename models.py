######### Creacion de Modelos de la Base de datos #########

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Minero(db.Model):
    id_minero = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    antiguedad = db.Column(db.Integer)
    cap_HR = db.Column(db.Integer)


class Produccion(db.Model):
    id_produccion = db.Column(db.Integer, primary_key=True)
    id_minero = db.Column(db.Integer, db.ForeignKey('minero.id_minero'))
    mes = db.Column(db.String(50))
    produccion = db.Column(db.Float)