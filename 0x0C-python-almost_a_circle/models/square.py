#!/usr/bin/python3
"""models/Square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """class Square"""
        return self.width

    @size.setter
    def size(self, value):
        """class Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """class Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """class Square"""
        if args:
            attr_names = ['id', 'size', 'x', 'y']
            for i, j in zip(attr_names, args):
                setattr(self, i, j)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """class Square"""
        d = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
        return d
