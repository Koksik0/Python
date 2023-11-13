import pytest
from triangles import Triangle
from Zestaw6.Zadanie2.points import Point


def test_triangle_creation():
    triangle = Triangle(0, 0, 1, 0, 0, 1)
    assert isinstance(triangle, Triangle)


def test_triangle_creation_from_points():
    points = [Point(0, 0), Point(1, 0), Point(0, 1)]
    triangle = Triangle.from_points(points)
    assert isinstance(triangle, Triangle)


def test_triangle_creation_collinear_points():
    with pytest.raises(ValueError):
        Triangle.from_points([Point(0, 0), Point(1, 1), Point(2, 2)])


def test_triangle_area():
    triangle = Triangle(0, 0, 3, 0, 0, 4)
    assert pytest.approx(triangle.area(), 1e-9) == 6.0


def test_triangle_move():
    triangle = Triangle(0, 0, 1, 0, 0, 1)
    triangle.move(2, 3)
    assert triangle.pt1 == Point(2, 3) and triangle.pt2 == Point(3, 3) and triangle.pt3 == Point(2, 4)


def test_triangle_make4():
    triangle = Triangle(0, 0, 1, 0, 0, 1)
    triangles = triangle.make4()
    assert all(isinstance(t, Triangle) for t in triangles) and len(triangles) == 4


def test_triangle_attributes():
    triangle = Triangle(0, 0, 3, 0, 0, 4)
    assert triangle.top == 0
    assert triangle.left == 0
    assert triangle.bottom == 4
    assert triangle.right == 3
    assert triangle.width == 3
    assert triangle.height == 4
    assert triangle.topleft == Point(0, 0)
    assert triangle.bottomleft == Point(0, 4)
    assert triangle.topright == Point(3, 0)
    assert triangle.bottomright == Point(3, 4)
