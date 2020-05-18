class Items:
    """Items in the vending macheine."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Item: {self.name}, costs ${self.price}, with {self.quantity} left"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.price!r}, {self.quantity!r})"
        )

    def display_items(self):
        print(self)

    def check_money(self):
        return self.price

    def purchase_item(self):
        print(f"You have purchased: {self.name}, enjoy!")
        self.quantity -= self.quantity
