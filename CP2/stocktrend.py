__author__ = 'Hernan Y.Ke'


class K:
    def __init__(self, symbol):
        self.price_his = []
        self.symbol = symbol

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("error")
        self.price_his.append(price)

    @property
    def price(self):
        return self.price_his[-1] if self.price_his else None

    def is_increasing(self):
        return self.price_his[-3] < self.price_his[-2] < self.price_his[-1]


