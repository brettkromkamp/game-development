"""
vector.py. Part of the 'game development' series

December 07, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from __future__ import annotations

import math

# ========== VECTOR2 ==========


class Vector2:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

    def length(self) -> float:  # Also known as 'magnitude'
        length = math.sqrt(self.x * self.x + self.y * self.y)  # https://en.wikipedia.org/wiki/Pythagorean_theorem
        return length

    def length_sqr(self) -> float:
        length = self.x * self.x + self.y * self.y
        return length

    # Scale up
    def __mul__(self, s: float) -> Vector2:  # 's' in this context is called a 'scalar' (a value representing only magnitude)
        scaled = Vector2()
        scaled.x = self.x * 2
        scaled.y = self.y * 2
        return scaled

    # Scale down
    def __truediv__(self, s: float) -> Vector2:
        scaled = Vector2()
        scaled.x = self.x / 2
        scaled.y = self.y / 2
        return scaled


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


# ========== EXECUTION ==========

if __name__ == "__main__":
    print("Start execution")

    # Adding a velocity vector to a (2D) point to calculate its new position
    point1 = Point(1.0, 0.0)
    velocity_vector1 = Vector2(2.0, 3.0)
    point2 = point1.add_vector(velocity_vector1)
    print(f"Result: {point2.x}, {point2.y}")

    # Calculate a direction (or offset) vector between two (2D) points
    point3 = Point(0.0, -1.0)
    point4 = Point(1.0, 1.0)
    direction_vector1 = point3 - point4
    print(f"Result: {direction_vector1.x}, {direction_vector1.y}")

    # Calculate the length of a vector
    print(f"Result: {direction_vector1.length()}")

    # Calculate the distance between multiple points (without using the 'expensive' SQRT function)
    point5 = Point(2.0, -1.0)
    direction_vector2 = point3 - point5
    direction_vector3 = point3 - point4
    print(f"Result: {direction_vector2.length_sqr()}, {direction_vector3.length_sqr()}")

    # Scale a vector up or down
    velocity_vector2 = Vector2(3.0, 4.0)
    vector_doubled = velocity_vector2 * 2
    vector_halved = velocity_vector2 / 2
    print(
        f"Result: {velocity_vector2.length()}, {vector_doubled.length()}, {vector_halved.length()}"
    )

    print("Finished execution")
