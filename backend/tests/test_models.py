import unittest
from app import create_app, db
from app.models import Inventario, Venta

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_inventario_creation(self):
        producto = Inventario(nombre_producto='Producto Test', cantidad=10, precio=9.99)
        db.session.add(producto)
        db.session.commit()
        self.assertEqual(producto.nombre_producto, 'Producto Test')

if __name__ == '__main__':
    unittest.main()
