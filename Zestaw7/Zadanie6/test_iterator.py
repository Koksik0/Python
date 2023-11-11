import unittest
from iterator import Binary_iterator, Random_iterator, Weekly_iterator


class TestIterator(unittest.TestCase):
    def setUp(self):
        self.binary_iterator = Binary_iterator()
        self.random_iterator = Random_iterator()
        self.weekly_iterator = Weekly_iterator()

    def test_binary_iterator(self):
        result = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        self.assertEqual([next(self.binary_iterator) for _ in range(10)], result)

    def test_weekly_iterator(self):
        result = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4]
        self.assertEqual([next(self.weekly_iterator) for _ in range(12)], result)


if __name__ == '__main__':
    unittest.main()
