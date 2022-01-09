class stock:

    def __init__(self, cost, quantity):
        self.quantity = int(quantity)
        self.dca = float(cost)

    def add_position(self, cost, quantity):
        last_quantity = self.quantity
        self.quantity += quantity
        self.dca = self.dca * (last_quantity/self.quantity) + cost * (quantity/self.quantity)

    def remove_position(self, quantity):
        self.quantity -= quantity
