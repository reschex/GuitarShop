class Order():
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if quantity > product.number_available():
            raise ValueError("Insufficient stock of \
{}. Only {} currently available.".format(product.description,
                                         product.number_available()))
        product.hold += quantity
        self.items[product] = quantity

    def remove_item(self, product):
        product.hold = product.hold - self.items[product]
        self.items.pop(product)
