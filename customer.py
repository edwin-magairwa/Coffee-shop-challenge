from coffee import Coffee
from order import Order

class Customer:
    def __init__(self, name):
        self.name = name  # Uses setter for validation

    @property
    def name(self):
        return self._name

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):

    @name.setter
    def name(self, value):
     if  not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]
       if  not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

            raise ValueError("Coffee must be a Coffee instance")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("Argument must be a Coffee instance")
        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price
        return max(customer_spending.items(), key=lambda x: x[1])[0] if customer_spending else None