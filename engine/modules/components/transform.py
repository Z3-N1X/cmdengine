from typing import TYPE_CHECKING
from . import Component
from varTypes.Vector2 import Vector2

if TYPE_CHECKING:
    from modules.gameObject import Object

class Transform(Component):
    def __init__(self):
        super().__init__()
        self._position: Vector2 = Vector2(0, 0)
        self._size: Vector2 = Vector2(1, 1)
    
    @property
    def position(self) -> Vector2:
        return self._position
    
    @position.setter
    def position(self, value: Vector2):
        if type(value.x) != int or type(value.y) != int:
            raise ValueError("Position must be an integer")
        self._position = value

    @property
    def size(self) -> Vector2:
        return self._size
    
    @size.setter
    def size(self, value: Vector2):
        self._size = value
