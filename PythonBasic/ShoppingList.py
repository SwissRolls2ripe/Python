class ShoppingList:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    def get_item_count(self):
        return len(self.shopping_list)

    def get_total_price(self):
        total = 0
        for item in self.shopping_list.values():
            total += item
        return total
