"""
main.py. Part of the 'game development' series

December 08, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""


from vector import Vector2
from point import Point


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

    # Scale a vector up or down to, for example, increase or decrease the velocity (speed) of an in-game object
    velocity_vector2 = Vector2(3.0, 4.0)
    vector_doubled = velocity_vector2 * 2
    vector_halved = velocity_vector2 / 2
    print(
        f"Result: {velocity_vector2.length()}, {vector_doubled.length()}, {vector_halved.length()}"
    )

    # Vector normalization
    point6 = Point(3.0, 4.0)
    point7 = Point(1.0, 2.0)

    vector1 = point6 - point7
    normalized_vector = vector1.normalized()
    print(f"Result: {normalized_vector.x}, {normalized_vector.y}, {normalized_vector.length()}")

    print("Finished execution")
