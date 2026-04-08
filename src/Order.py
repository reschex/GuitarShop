class Order():
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if quantity > product.stock:
            raise ValueError("Insufficient stock of \
{}. Only {} currently available.".format(product.description, product.stock))
        product.hold += quantity
        self.items.append({product: quantity})
