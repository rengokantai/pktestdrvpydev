__author__ = 'Hernan Y.Ke'
import unittest
from datetime import datetime
from ..stocktrend import K

class KTrendTest(unittest.TestCase):
    def setUp(self):
        self.ke = K("k")
    def given_a_series(self,prices):
        tss = [datetime(2016, 6, 18),datetime(2016, 6, 19),datetime(2016, 6, 20)]
        for ts,price in zip(tss, prices):
            self.ke.update(ts,price)
    def test_increasing_trend_is_true(self):
        self.given_a_series([1,2,3])
        self.assertTrue(self.ke.is_increasing())
    def test_decreasing_trend_is_true(self):
        self.given_a_series([2,1,0])
        self.assertFalse(self.ke.is_increasing())




if __name__ == '__main__':
    unittest.main()