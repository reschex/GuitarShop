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
        # this doesn't feel very readable in isolation
        # want to add product quantity into this somehow
        product.hold = product.hold - self.items[product]
        self.items.pop(product)

    def get_item_total(self):
        total = 0
        for item, quantity in self.items.items():
            total += item.price * quantity
        return total

    def confirm(self):
        for item, quantity in self.items.items():
            item.stock -= quantity
            item.hold -= quantity
