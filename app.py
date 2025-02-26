import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definición del modelo de la tabla 'estudiantes'
class Estudiante(db.Model):
    __tablename__ = 'alumnos'
    no_control = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=True)
    ap_paterno = db.Column(db.String, nullable=True)
    ap_materno = db.Column(db.String, nullable=True)
    semestre = db.Column(db.Integer, nullable=True)

# Endpoint para obtener todos los estudiantes
@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    estudiantes = Estudiante.query.all()
    lista_estudiantes = []
    for estudiante in estudiantes:
        lista_estudiantes.append({
            'no_control': estudiante.no_control,
            'nombre': estudiante.nombre,
            'ap_paterno': estudiante.ap_paterno,
            'ap_materno': estudiante.ap_materno,
            'semestre': estudiante.semestre
        })
    return jsonify(lista_estudiantes)

if __name__ == '__main__':
    app.run(debug=True)