__author__ = 'Hernan Y.Ke'
class K:
    def __init__(self,symbol):
        self.price=None
        self.symbol=symbol
    def update(self,timestamp,price):
        if price<0:
            raise ValueError("error")
        self.price=price


