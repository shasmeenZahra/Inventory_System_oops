import datetime

class Product:
    def __init__(self, product_id, name, price, quantity, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.added_on = datetime.datetime.now()

    def to_dict(self):
        return {
            "Product ID": self.product_id,
            "Name": self.name,
            "Price": self.price,
            "Quantity": self.quantity,
            "Category": self.category,
            "Added On": self.added_on.strftime("%Y-%m-%d %H:%M:%S")
        }
