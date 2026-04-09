class Order():
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        available_items = product.stock - product.hold
        if quantity > available_items:
            raise ValueError("Insufficient stock of \
{}. Only {} currently available.".format(product.description, available_items))
        product.hold += quantity
        self.items.append({product: quantity})
