from flask import Flask, render_template
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mineros.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

########### MODELS ###########
class Minero(db.Model):
    id_minero = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    antiguedad = db.Column(db.Integer)
    produccion_enero = db.Column(db.Float)
    produccion_febrero = db.Column(db.Float)
    produccion_marzo = db.Column(db.Float)
    cap_HR = db.Column(db.Integer)
    

# create tables
with app.app_context():
    db.create_all()

# populate database
with app.app_context():
    # Populate database
    minero1 = Minero(marca="Bitmain", modelo="S9", antiguedad=2, produccion_enero=15, produccion_febrero=18, produccion_marzo=25, cap_HR=18)
    minero2 = Minero(marca="Bitmain", modelo="S9", antiguedad=3, produccion_enero=0.3, produccion_febrero=5, produccion_marzo=7, cap_HR=12)
    # add objects to session
    db.session.add(minero1)
    db.session.add(minero2)
    # commit the changes
    db.session.commit()


########### ROUTES ###########
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/grafico/<tipo>")
def grafico(tipo):
    if tipo == "barras":
        tipo = "bar"
    else:
        tipo = "pie"
        
    if tipo == "bar":
        datos = { 
                    "ciudades": ["Asuncion", "Ciudad del Este", "Encarnacion"],
                    "estudiantes" :[900, 200, 300]
                }
        
        # parse dictionary to json
        datos_json = json.dumps(datos)
        return render_template("graficos.html", datos_json=datos_json, tipo=tipo)
    
    else:

        datos2 = {
                    "ciudades": ["San Lorenzo", "San Pedro", "San Juan"],
                    "estudiantes" :[100, 200, 300]
                }
        
        # parse dictionary to json
        datos_json = json.dumps(datos2)

        return render_template("graficos.html", datos_json=datos_json, tipo=tipo)

@app.route("/mineros")
def mineros():
    mineros = Minero.query.all()
    return render_template("mineros.html", mineros=mineros)

@app.route("/mineros/<id_minero>")
def minero(id_minero):
    minero = Minero.query.get(id_minero)
    print(minero.marca)

    data_minero = {
        "meses": ["Enero", "Febrero", "Marzo"],
        "produccion": [minero.produccion_enero, minero.produccion_febrero, minero.produccion_marzo]
    }

    data_minero_json = json.dumps(data_minero)


    return render_template("minero.html", data_minero_json=data_minero_json, minero=minero)


# BREAKPOINT

if __name__ == "__main__":
    app.run(debug=True)