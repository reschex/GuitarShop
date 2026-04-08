from src.Order import Order
from src.Product import Product


class TestGuitarShop():

    # Then a temporary hold for the sale quantity is placed
    # on that product’s stock
    def test_hold_is_placed_when_product_added_to_an_order(self):
        order = Order()
        product = Product(327, 7, 0)
        order.add_item(product, 1)
        assert product.hold == 1

    # And a new item is added to the order’s items list
    # with that product and sale quantity
    def test_new_item_is_added_to_orders_item_list(self):
        order = Order()
        product = Product(327, 7, 0)
        order.add_item(product, 1)
        assert order.items[0] == {product: 1}
