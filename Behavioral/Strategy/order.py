class Item:

    def __init__(self, price, discount_strategy = None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):

        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount

    def __repr__(self):
        statement = "Price: {}, price after discount: {}"
        return statement.format(self.price, self.price_after_discount())


def twenty_percent_discount(order):
    return order.price * 0.2


def on_sale_discount(order):
    return order.price * 0.25 + 20
