"""
point.py. Part of the 'game development' series

December 08, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from __future__ import annotations

from vector import Vector2


# ========== POINT ==========


class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

    def add_vector(self, v: Vector2) -> Point:
        p2 = Point()
        p2.x = self.x + v.x
        p2.y = self.y + v.y
        return p2

    def __sub__(self, other: Point) -> Vector2:
        v = Vector2()
        v.x = self.x - other.x
        v.y = self.y - other.y
        return v
