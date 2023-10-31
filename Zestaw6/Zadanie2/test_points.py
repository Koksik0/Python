import math
import unittest
from points import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.first_point = Point(1, 2)
        self.second_point = Point(4, 7)

    def test_eq_points(self):
        self.assertEqual(self.first_point.__eq__(self.second_point), False)

    def test_ne_points(self):
        self.assertEqual(self.first_point.__ne__(self.second_point), True)

    def test_add_points(self):
        point = Point(5, 9)
        self.assertEqual(self.first_point.__add__(self.second_point), point)

    def test_sub_points(self):
        point = Point(-3,-5)
        self.assertEqual(self.first_point.__sub__(self.second_point), point)

    def test_mul_points(self):
        self.assertEqual(self.first_point.__mul__(self.second_point), 18)

    def test_cross_points(self):
        self.assertEqual(self.first_point.cross(self.second_point), -1)

    def test_length_points(self):
        self.assertEqual(self.first_point.length(), math.sqrt(5))
        self.assertEqual(self.second_point.length(), math.sqrt(65))


if __name__ == '__main__':
    unittest.main()
