import math

from Zestaw6.Zadanie2.points import Point


class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        if x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0:
            raise ValueError("Punkty nie powinny leżeć na jednej prostej")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]"

    def __repr__(self):
        return f"Triangle({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})"

    def __eq__(self, other):
        if self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y and self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y and self.pt3.x == other.pt3.x and self.pt3.y == other.pt3.y:
            return True
        return False

    def __ne__(self, other):
        return not self == other

    def center(self) -> Point:
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self):
        len_a = Point.length(Point(self.pt2.x - self.pt1.x, self.pt2.y - self.pt1.y))
        len_b = Point.length(Point(self.pt3.x - self.pt2.x, self.pt3.y - self.pt2.y))
        len_c = Point.length(Point(self.pt3.x - self.pt1.x, self.pt3.y - self.pt1.y))
        p = (len_a + len_b + len_c) / 2
        return math.sqrt(p * (p - len_a) * (p - len_b) * (p - len_c))

    def move(self, x, y):
        self.pt1.x += x
        self.pt2.x += x
        self.pt3.x += x
        self.pt1.y += y
        self.pt2.y += y
        self.pt3.y += y

    def make4(self) -> tuple:
        middle_a_x = (self.pt2.x + self.pt1.x) / 2
        middle_a_y = (self.pt2.y + self.pt1.y) / 2
        middle_b_x = (self.pt3.x + self.pt2.x) / 2
        middle_b_y = (self.pt3.y + self.pt2.y) / 2
        middle_c_x = (self.pt3.x + self.pt1.x) / 2
        middle_c_y = (self.pt3.y + self.pt1.y) / 2

        triangle1 = Triangle(self.pt1.x, self.pt1.y, middle_a_x, middle_a_y, middle_c_x, middle_c_y)
        triangle2 = Triangle(self.pt2.x, self.pt2.y, middle_a_x, middle_a_y, middle_b_x, middle_b_y)
        triangle3 = Triangle(self.pt3.x, self.pt3.y, middle_b_x, middle_b_y, middle_c_x, middle_c_y)
        triangle4 = Triangle(middle_a_x, middle_a_y, middle_b_x, middle_b_y, middle_c_x, middle_c_y)
        return (triangle1, triangle2, triangle3, triangle4)


