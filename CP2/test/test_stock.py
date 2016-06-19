__author__ = 'Hernan Y.Ke'
import unittest
from datetime import datetime
from ..stock import K


class KTest(unittest.TestCase):
    def setUp(self):
        self.ke = K("k")
    def test_ke(self):
        self.assertIsNone(self.ke.price)

    def test_ke_update(self):
        self.ke.update(datetime(2016, 6, 18), 100)
        self.assertEqual(100, self.ke.price)

    def test_negative_throw(self):
        with self.assertRaises(ValueError):
            self.ke.update(datetime(2016, 6, 18), -1)

    def test_almostequal(self):
        self.ke.update(datetime(2016, 6, 18), 100.1)
        self.assertAlmostEqual(100.12,self.ke.price,places=1)
        # places, or delta=0.01


if __name__ == '__main__':
    unittest.main()