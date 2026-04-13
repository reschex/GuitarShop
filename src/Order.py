from src.Regions import Regions


class Order():
    def __init__(self):
        self.items = {}
        self.status = "Open"
        self.country = "England"

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
        self.status = "Confirmed"

    def get_shipping_cost(self):
        regions = Regions()
        shipping_under_onehundred = {
            "UK": 5.99,
            "EU": 9.99,
            "Other": 12.99
        }
        shipping_over_onehundred = {
            "UK": 0,
            "EU": 5.99,
            "Other": 9.99
        }

        if self.get_item_total() >= 100:
            return shipping_over_onehundred[regions.get_region_of
                                            (self.country)]
        else:
            return shipping_under_onehundred[regions.get_region_of
                                             (self.country)]
