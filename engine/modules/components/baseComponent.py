from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .. import Object

class Component:
    def __init__(self):
        self.name = None
        self.parent = None

