"""Lab 9 tests - run from the project root with: python -m unittest discover tests"""
import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from supplier import Supplier
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from inventory import Inventory
from order import Order
from orderline import OrderLine
from discount import (DiscountStrategy, NoDiscount, PercentageDiscount,
                      BulkDiscount, StudentDiscount)
from productfactory import ProductFactory
from helpers import get_positive_float, load_products


def make_supplier() -> Supplier:
    return Supplier("S001", "TechWorld", "sales@techworld.sg")


class TestDiscounts(unittest.TestCase):
    def setUp(self):
        self.product = PhysicalProduct("P1", "Item", 50.0, 10, make_supplier(), 1.0)

    def make_order(self, discount=None) -> Order:
        order = Order("O1", discount)
        order.add_order_line(self.product, 5)  # total 250
        return order

    def test_default_is_no_discount(self):
        self.assertEqual(self.make_order().calculate_total(), 250)

    def test_bulk_discount(self):
        self.assertEqual(self.make_order(BulkDiscount(200, 20)).calculate_total(), 230)

    def test_bulk_below_threshold(self):
        order = Order("O2", BulkDiscount(200, 20))
        order.add_order_line(self.product, 1)
        self.assertEqual(order.calculate_total(), 50)

    def test_percentage_discount(self):
        self.assertAlmostEqual(self.make_order(PercentageDiscount(10)).calculate_total(), 225)

    def test_set_discount_changes_strategy(self):
        order = self.make_order(BulkDiscount(200, 20))
        self.assertEqual(order.calculate_total(), 230)
        order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 225)

    def test_new_strategy_needs_no_order_change(self):
        self.assertAlmostEqual(self.make_order(StudentDiscount()).calculate_total(), 237.5)

    def test_strategies_are_discount_strategies(self):
        for s in (NoDiscount(), PercentageDiscount(5), BulkDiscount(1, 1), StudentDiscount()):
            self.assertIsInstance(s, DiscountStrategy)

    def test_invalid_percentage_rejected(self):
        with self.assertRaises(ValueError):
            PercentageDiscount(150)


class TestFactory(unittest.TestCase):
    def test_creates_physical(self):
        p = ProductFactory.create("physical", "P1", "Lamp", 25.0, 10, make_supplier(), 1.5)
        self.assertIsInstance(p, PhysicalProduct)

    def test_creates_digital(self):
        p = ProductFactory.create("digital", "D1", "Ebook", 10.0, 10, make_supplier(), 20.0)
        self.assertIsInstance(p, DigitalProduct)

    def test_unknown_type_raises(self):
        with self.assertRaises(ValueError) as ctx:
            ProductFactory.create("service", "S1", "Install", 30.0, 5, make_supplier())
        self.assertIn("Unknown product type", str(ctx.exception))


class TestValidation(unittest.TestCase):
    def test_price_must_be_positive(self):
        for bad in (0, -5):
            with self.assertRaises(ValueError):
                ProductFactory.create("physical", "P1", "X", bad, 1, make_supplier())

    def test_stock_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("digital", "D1", "X", 5.0, -1, make_supplier())

    def test_update_stock_cannot_go_negative(self):
        p = ProductFactory.create("digital", "D1", "X", 5.0, 2, make_supplier())
        with self.assertRaises(ValueError):
            p.update_stock(-3)

    def test_order_line_quantity_must_be_positive(self):
        p = ProductFactory.create("physical", "P1", "X", 5.0, 5, make_supplier())
        for bad in (0, -2):
            with self.assertRaises(ValueError):
                OrderLine(p, bad)


class TestUserInput(unittest.TestCase):
    def test_retries_until_valid(self):
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
            with redirect_stdout(io.StringIO()) as out:
                value = get_positive_float("Price: ")
        self.assertEqual(value, 12.5)
        self.assertIn("valid number", out.getvalue())
        self.assertIn("greater than zero", out.getvalue())


class TestLoadProducts(unittest.TestCase):
    CSV = ("product_type,product_id,name,price,stock_quantity\n"
           "physical,P001,Desk Lamp,25.00,10\n"
           "digital,D001,Photo Editor,49.90,100\n"
           "service,S001,Installation,30.00,5\n"
           "physical,P002,Office Chair,abc,3\n"
           "physical,P003,Monitor Stand,39.50,7\n")

    def test_bad_rows_skipped_valid_rows_loaded(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "products.csv")
            with open(path, "w", newline="") as f:
                f.write(self.CSV)
            inventory = Inventory()
            with redirect_stdout(io.StringIO()) as out:
                load_products(path, inventory, make_supplier())
        self.assertEqual(len(inventory.get_products()), 3)
        self.assertIn("3 products loaded.", out.getvalue())
        self.assertIn("Load attempt finished.", out.getvalue())

    def test_missing_file_handled(self):
        inventory = Inventory()
        with redirect_stdout(io.StringIO()) as out:
            load_products("does_not_exist.csv", inventory, make_supplier())
        self.assertEqual(len(inventory.get_products()), 0)
        self.assertIn("not found", out.getvalue())
        self.assertIn("Load attempt finished.", out.getvalue())


if __name__ == "__main__":
    unittest.main()