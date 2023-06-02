class Customer:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer is self]

    
    def coffees(self):
        return list({order.coffee for order in self.orders()})

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise AttributeError

    def create_order(self, coffee, price):
        Order(self, coffee, price)
        
from classes.order import Order