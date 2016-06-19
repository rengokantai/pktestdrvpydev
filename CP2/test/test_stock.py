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

    def test_negative_throw(self):
        ke = K("k")
        try:
            ke.update(datetime(2016, 6, 18), -1)
        except ValueError:
            return
        self.fail("not raised error")


if __name__ == '__main__':
    unittest.main()