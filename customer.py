from order import Order

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order  # Local import to avoid circular dependency
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        customers = coffee.customers()
        if not customers:
            return None
        return max(customers, key=lambda c: sum(order.price for order in Order.all if order.customer == c and order.coffee == coffee))
