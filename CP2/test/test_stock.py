__author__ = 'Hernan Y.Ke'
import unittest
from datetime import datetime
from ..stock import K


class KTest(unittest.TestCase):
    def test_ke(self):
        ke = K("k")
        self.assertIsNone(ke.price)

    def test_ke_update(self):
        ke = K("k")
        ke.update(datetime(2016, 6, 18), 100)
        self.assertEqual(100, ke.price)


if __name__ == '__main__':
    unittest.main()