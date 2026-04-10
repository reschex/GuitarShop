from src.Order import Order
from src.Product import Product
import pytest


class TestAddItem():

    # Then a temporary hold for the sale quantity is placed
    # on that product’s stock
    def test_hold_is_placed(self):
        order = Order()
        product = Product(327, stock=7)
        order.add_item(product, 1)
        assert product.hold == 1

    # And a new item is added to the order’s items list
    # with that product and sale quantity
    def test_new_item_is_added_to_orders_item_list(self):
        order = Order()
        product = Product(327, stock=7)
        order.add_item(product, 1)
        assert order.items[product] == 1

    # Then an error is raised that the product has insufficient stock
    def test_insufficient_stock_error_is_raised(self):
        order = Order()
        product = Product(327, description="Ibanez Tube Screamer", stock=1)
        with pytest.raises(ValueError, match="Ibanez Tube Screamer.+1"):
            order.add_item(product, 2)
        assert len(order.items) == 0
        assert product.hold == 0

    # Insufficient available product stock, stock on hold
    # And has specified a sale quantity that is greater than that product’s
    # availablen stock minus the amount of stock on hold,
    # Then an error is raised that the product has insufficient stock
    def test_insufficient_stock_error_when_stock_on_hold(self):
        order = Order()
        product = Product(327,
                          description="Ibanez Tube Screamer",
                          stock=2,
                          hold=1)
        with pytest.raises(ValueError, match="Ibanez Tube Screamer.+1"):
            order.add_item(product, 2)


class TestRemoveItem():

    # Then the temporary hold for the item quantity is released
    # on that product’s stock
    def test_release_hold_on_product(self):
        order = Order()
        product = Product(327, stock=2)
        order.add_item(product=product, quantity=2)
        order.remove_item(product)
        assert product.hold == 0

    # And the item is removed from the order’s items list
    def test_remove_from_order_list(self):
        order = Order()
        product = Product(327, stock=2)
        order.add_item(product=product, quantity=2)
        order.remove_item(product)
        assert len(order.items) == 0


class TestTotalNotIncludingShipping():
    def test_no_items_total_is_zero(self):
        order = Order()
        assert order.get_item_total() == 0

    def test_one_item_total(self):
        order = Order()
        product = Product(327, stock=2, price=159.95)
        order.add_item(product=product, quantity=1)
        assert order.get_item_total() == product.price

    def test_two_items_with_quantity_of_one(self):
        order = Order()
        guitar1 = Product(327, stock=7, price=159.95)
        guitar2 = Product(811, stock=2, price=1799.00)
        order.add_item(guitar1, 1)
        order.add_item(guitar2, 1)
        assert order.get_item_total() == guitar1.price + guitar2.price

    def test_one_item_with_quantity_greater_than_one(self):
        order = Order()
        guitar1 = Product(327, stock=2, price=159.95)
        order.add_item(guitar1, 2)
        assert order.get_item_total() == guitar1.price * 2


class TestConfirmOrder():
    # Then the stock of each item’s product as adjusted by the item quantity
    def test_stock_is_reduced_by_quantity(self):
        order = Order()
        product1 = Product(327, stock=7)
        product2 = Product(811, stock=2)
        order.add_item(product1, 2)
        order.add_item(product2, 1)
        order.confirm()
        assert product1.stock == 5
        assert product2.stock == 1

    # And the hold on each stock is reduced by the item quantity
    def test_hold_is_reduced_by_quantity(self):
        order = Order()
        product1 = Product(327, stock=7)
        product2 = Product(811, stock=2)
        order.add_item(product1, 2)
        order.add_item(product2, 1)
        order.confirm()
        assert product1.hold == 0
        assert product2.hold == 0

    # And the order’s status is set to Confirmed
    def test_order_status_confirmed(self):
        order = Order()
        product1 = Product(327, stock=7)
        order.add_item(product1, 2)
        assert order.status == "Open"
        order.confirm()
        assert order.status == "Confirmed"
