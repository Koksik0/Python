import math
import unittest
from triangles import Triangle
from Zestaw6.Zadanie2.points import Point


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.first = Triangle(0, 0, 2, 0, 1, 2)

    def test__eq__(self):
        self.assertEqual(Triangle(1, 1, 2, 2, 3, 3),
                         Triangle(1, 1, 2, 2, 3, 3))

    def test_center(self):
        self.assertEqual(self.first.center(), Point(1.0, 0.6666666666666666))

    def test_area(self):
        self.assertEqual(self.first.area(), 2.0)

    def test_move(self):
        self.first.move(1, 1)
        self.assertEqual(self.first, Triangle(1, 1, 3, 1, 2, 3))

    def test_make4(self):
        self.assertEqual(self.first.make4(), (Triangle(0, 0, 1, 0, 0.5, 1),
                                              Triangle(2, 0, 1, 0, 1.5, 1),
                                              Triangle(1, 2, 1.5, 1, 0.5, 1),
                                              Triangle(1, 0, 1.5, 1, 0.5, 1)))


if __name__ == '__main__':
    unittest.main()
