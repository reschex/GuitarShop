class Product():
    def __init__(self, id, description="", stock=0, hold=0, price=0.00):
        self.id = id
        self.description = description
        self.stock = stock
        self.hold = hold
        self.price = price

    def number_available(self):
        return self.stock - self.hold
