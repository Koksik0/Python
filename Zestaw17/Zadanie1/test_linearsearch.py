import unittest
from linearsearch import LinearSearch


class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        self.list = LinearSearch(10, 100)

    def test_search(self):
        self.assertEqual(self.list.search(11), ValueError("Błędna Liczba"))


if __name__ == '__main__':
    unittest.main()