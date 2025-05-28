"""
    Vector2 is a class that represents a 2D vector.
    It is used to store the position of an object in the game.
"""
class Vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector2({self.x}, {self.y})"
