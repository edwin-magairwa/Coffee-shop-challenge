import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("A" * 16)
        with self.assertRaises(ValueError):
            Customer(123)

    def test_orders(self):
        order = self.customer.create_order(self.coffee, 5.0)
        self.assertEqual(self.customer.orders(), [order])

    def test_coffees(self):
        self.customer.create_order(self.coffee, 5.0)
        self.assertEqual(self.customer.coffees(), [self.coffee])

    def test_most_aficionado(self):
        c2 = Customer("Bob")
        self.customer.create_order(self.coffee, 5.0)
        c2.create_order(self.coffee, 10.0)
        self.assertEqual(Customer.most_aficionado(self.coffee), c2)

if __name__ == '__main__':
    unittest.main()