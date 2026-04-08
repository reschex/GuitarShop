from src.Order import Order
from src.Product import Product


class TestGuitarShop():

    def test_hold_is_placed_when_product_added_to_an_order(self):
        product = Product(327, 7, 0)
        order = Order()
        order.add_item(product, 1)
        assert product.hold == 1
