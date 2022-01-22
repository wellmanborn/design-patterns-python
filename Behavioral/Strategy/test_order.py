from Behavioral.Strategy.order import Item, twenty_percent_discount, on_sale_discount


class TestOrder:
    def test_order(self):
        assert Item(20000).price == 20000
        assert Item(20000, discount_strategy=twenty_percent_discount).price_after_discount() == 16000.0
        assert Item(20000, discount_strategy=on_sale_discount).price_after_discount() == 14980.0