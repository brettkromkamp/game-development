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
        length = math.sqrt(
            self.x * self.x + self.y * self.y
        )  # https://en.wikipedia.org/wiki/Pythagorean_theorem
        return length

    def length_sqr(self) -> float:
        length = self.x * self.x + self.y * self.y
        return length

    # Scale up
    def __mul__(
        self, s: float
    ) -> Vector2:  # 's' in this context is called a 'scalar' (a value representing only magnitude)
        scaled = Vector2()
        scaled.x = self.x * s
        scaled.y = self.y * s
        return scaled

    # Scale down
    def __truediv__(self, s: float) -> Vector2:
        scaled = Vector2()
        scaled.x = self.x / s
        scaled.y = self.y / s
        return scaled

    # Normalized (or unit-length or normal-length) vector
    def normalized(self):
        # https://en.wikibooks.org/wiki/Guide_to_Game_Development/Theory/Mathematics/Vectors#Unit_length_vector
        normalized = self / self.length()  # Vector2
        return normalized
