import unittest
from binarysearch import BinarySearch


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.n = 100
        self.list = BinarySearch(self.n)

    def test_binare_rek(self):
        self.assertEqual(self.list.binarne_rek(0, self.n - 1, 10), 5)
        self.assertEqual(self.list.binarne_rek(0, self.n - 1, 9), -1)


if __name__ == '__main__':
    unittest.main()
