import unittest
from ShoppingList import ShoppingList

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"pen" : 50, "book" : 30, "computer" : 3000})

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 2)

    def test_get_total_price(self):
        self.assertGreater(self.shopping_list.get_total_price(), 9000, msg=None)