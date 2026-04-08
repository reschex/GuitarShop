class Order():
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        product.hold += quantity
        self.items.append({product: quantity})
