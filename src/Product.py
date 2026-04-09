class Product():
    def __init__(self, id, description, stock, hold, price):
        self.id = id
        self.description = description
        self.stock = stock
        self.hold = hold
        self.price = price

    def number_available(self):
        return self.stock - self.hold
