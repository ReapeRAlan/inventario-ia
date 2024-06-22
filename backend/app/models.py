from . import db
from datetime import datetime

class Inventario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    fecha_ultima_actualizacion = db.Column(db.DateTime, default=datetime.utcnow)

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('inventario.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha_venta = db.Column(db.DateTime, default=datetime.utcnow)
