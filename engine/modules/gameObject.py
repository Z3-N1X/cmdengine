from typing import Self, List
from .components.baseComponent import Component
from varTypes.Vector2 import Vector2
from .components.transform import Transform

# Object is the base class for all game objects
# It is used to create and manage game objects
class Object:
    def __init__(self, name: str, active: bool = True, parent: Self = None):
        self.name = name
        self.active = active
        self._parent = parent
        self.children = []
        self.components: List[Component] = []
        self.sprite = '.'

    @property
    def parent(self) -> Self:
        return self._parent

    @parent.setter
    def parent(self, value: Self):
        if value == self:
            raise ValueError("Object cannot be its own parent")
        self._parent = value

    def add_child(self, child: Self):
        self.children.append(child)
        child.parent = self
