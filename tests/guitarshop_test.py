class Product():
    def __init__(self, id, stock, hold):
        self.id = id
        self.stock = stock
        self.hold = hold


class Order():
    def __init__(self):
        pass

    def add_item(self, product, quantity):
        product.hold += 1


class TestGuitarShop():
    def test_basic(self):
        assert 1 == 1

    def test_hold_is_placed_when_product_added_to_an_order(self):
        product = Product(327, 7, 0)
        order = Order()
        order.add_item(product, 1)
        assert product.hold == 1
