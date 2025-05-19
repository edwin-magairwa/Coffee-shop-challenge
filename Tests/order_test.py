import unittest
from customer import Customer
from coffee import Coffee
from order import Order
class TestOrder(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")
    def test_price_validation(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)
    with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, "5.0")

    def test_immutable_price(self):
        order = Order(self.customer, self.coffee, 5.0)
        with self.assertRaises(AttributeError):
            order.price = 6.0

    def test_customer_and_coffee(self):
        order = Order(self.customer, self.coffee, 5.0)
        