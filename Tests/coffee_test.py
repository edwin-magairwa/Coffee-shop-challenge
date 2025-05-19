    with self.assertRaises(ValueError):
            Coffee("Ab")
        with self.assertRaises(ValueError):
            Coffee(123)

    def test_immutable_name(self):
        with self.assertRaises(AttributeError):
            self.coffee.name = "Latte"

    def test_orders(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(self.coffee.orders(), [order])

    def test_customers(self):
        Order(self.customer, self.coffee, 5.0)
        self.assertEqual(self.coffee.customers(), [self.customer])

    def test_num_orders(self):
        Order(self.customer, self.coffee, 5.0)
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        Order(self.customer, self.coffee, 5.0)
        Order(self.customer, self.coffee, 10.0)
        self.assertEqual(self.coffee.average_price(), 7.5)

if __name__ == '__main__':
    unittest.main()