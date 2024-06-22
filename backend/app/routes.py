from flask import Blueprint, jsonify, request
from .models import Inventario, Venta
from . import db

main = Blueprint('main', __name__)

@main.route('/inventario', methods=['GET'])
def get_inventario():
    inventario = Inventario.query.all()
    return jsonify([producto.to_dict() for producto in inventario])

@main.route('/inventario', methods=['POST'])
def add_producto():
    data = request.json
    nuevo_producto = Inventario(
        nombre_producto=data['nombre_producto'],
        cantidad=data['cantidad'],
        precio=data['precio']
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify(nuevo_producto.to_dict()), 201
