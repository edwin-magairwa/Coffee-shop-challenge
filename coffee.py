:from order import Order

class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters")
        self._name = name

    @property
    def name(self)
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Coffee name is immutable")

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

 