import unittest
from customer import Customer
from coffee import Coffee
from order import Order

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
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)

if __name__ == '__main__':
    unittest.main()