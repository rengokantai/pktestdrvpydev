__author__ = 'Hernan Y.Ke'
import unittest
from ..stock import K
class KTest(unittest.TestCase):
    def test_ke(self):
        ke = K("k")
        self.assertIsNone(ke.price)
if __name__ == '__main__':
    unittest.main()