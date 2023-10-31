from Zestaw6.Zadanie2.points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        if self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y and self.pt2.x == self.pt2.y:
            return True
        return False

    def __ne__(self, other):
        return not self == other

    def center(self) -> list:
        return [(self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2]

    def area(self) -> float:
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y
