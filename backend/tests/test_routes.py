import unittest
import json
from app import create_app, db
from app.models import Inventario

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_inventario(self):
        response = self.client.get('/inventario')
        self.assertEqual(response.status_code, 200)

    def test_add_producto(self):
        response = self.client.post('/inventario', data=json.dumps({
            'nombre_producto': 'Producto Test',
            'cantidad': 10,
            'precio': 9.99
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
