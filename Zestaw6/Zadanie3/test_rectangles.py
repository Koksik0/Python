import unittest
from rectangles import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.first_rectangle = Rectangle(1, 1, 3, 3)
        self.second_rectangle = Rectangle(2, 3, 6, 8)

    def test_eq_rectangles(self):
        self.assertEqual(self.first_rectangle.__eq__(self.second_rectangle), False)

    def test_ne_rectangles(self):
        self.assertEqual(self.first_rectangle.__ne__(self.second_rectangle), True)

    def test_centre_rectangles(self):
        self.assertEqual(self.first_rectangle.center(), [2, 2])
        self.assertEqual(self.second_rectangle.center(), [4, 5.5])

    def test_area_rectangles(self):
        self.assertEqual(self.first_rectangle.area(), 4)
        self.assertEqual(self.second_rectangle.area(), 20)

    def test_move_rectangles(self):
        self.first_rectangle.move(2, 2)
        self.second_rectangle.move(1, -1)
        self.assertEqual(self.first_rectangle, Rectangle(3, 3, 5, 5))
        self.assertEqual(self.second_rectangle, Rectangle(3, 2, 7, 7))


if __name__ == '__main__':
    unittest.main()
