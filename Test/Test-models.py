import unittest
from service.models import Product

class TestProductModel(unittest.TestCase):
    def test_read_product(self):
        # إنشاء منتج
        product = Product(id=1, name="Test Product", category="Test Category", available=True, price=9.99)

        # التحقق من القيم
        self.assertEqual(product.id, 1)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.category, "Test Category")
        self.assertTrue(product.available)
        self.assertEqual(product.price, 9.99)
