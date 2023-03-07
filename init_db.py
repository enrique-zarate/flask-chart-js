# inicializa la base de datos y crea las tablas

from models import db, Minero, Produccion
from flask import Flask

# crea la aplicacion
app = Flask('app')

# configura la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farming.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicializa la base de datos
db.init_app(app)

# crea las tablas
with app.app_context():
    db.create_all()

#####################################
# crea un minero y una produccion
# para efectos de ejemplo.
minero = Minero(marca="Antminer", modelo="S9", antiguedad=2, cap_HR=14.5)
produccion = Produccion(id_minero=1,mes="Enero", produccion=15.5)

# agrega el minero a la base de datos

with app.app_context():
    # guarda los cambios
    db.session.add(minero)
    db.session.add(produccion)
    db.session.commit()

