__author__ = 'Hernan Y.Ke'
import unittest
from datetime import datetime
from ..stocktrend import K

class KTrendTest(unittest.TestCase):
    def setUp(self):
        self.ke = K("k")
    def test_increase(self):
        tss = [datetime(2016, 6, 18),datetime(2016, 6, 19),datetime(2016, 6, 20)]
        prices = [1,2,3]
        for ts,price in zip(tss, prices):
            self.ke.update(ts,price)
        self.assertTrue(self.ke.is_increasing())



if __name__ == '__main__':
    unittest.main()