from customer import Customer
from coffee import Coffee
from order import Order

# Create some test data
c1 = Customer("Alice")
c2 = Customer("Bob")
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

# Create orders
order1 = c1.create_order(coffee1, 5.0)
order2 = c1.create_order(coffee2, 6.0)
order3 = c2.create_order(coffee1, 4.5)

# Test relationships and aggregates
print(f"{c1.name}'s orders: {[order.price for order in c1.orders()]}")
print(f"{coffee1.name}'s customers: {[customer.name for customer in coffee1.customers()]}")
print(f"{coffee1.name} order count: {coffee1.num_orders()}")
print(f"{coffee1.name} average price: {coffee1.average_price()}")
print(f"Most aficionado for {coffee1.name}: {Customer.most_aficionado(coffee1).name if Customer.most_aficionado(coffee1) else 'None'}")