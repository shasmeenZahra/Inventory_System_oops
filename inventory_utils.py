import pandas as pd

class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def update_quantity(self, product_id, qty):
        if product_id in self.products:
            self.products[product_id].quantity = qty

    def update_price(self, product_id, price):
        if product_id in self.products:
            self.products[product_id].price = price

    def get_product_list(self):
        return [p.to_dict() for p in self.products.values()]

    def search(self, keyword):
        return [p.to_dict() for p in self.products.values() if keyword.lower() in p.name.lower()]

    def low_stock(self, threshold):
        return [p.to_dict() for p in self.products.values() if p.quantity < threshold]

    def get_total_value(self):
        return sum(p.price * p.quantity for p in self.products.values())

    def to_dataframe(self):
        return pd.DataFrame(self.get_product_list())
