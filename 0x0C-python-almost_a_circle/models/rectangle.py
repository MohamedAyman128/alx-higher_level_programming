#!/usr/bin/python3
"""models/rectangle.py"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """class Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """class Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """class Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """class Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """class Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """class Rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """class Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """class Rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """class Rectangle"""
        return self.__height * self.__width

    def display(self):
        """class Rectangle"""
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """class Rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """class Rectangle"""
        if args:
            attr_names = ['id', 'width', 'height', 'x', 'y']
            for i, j in zip(attr_names, args):
                setattr(self, i, j)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """class Rectangle"""
        d = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
        return d
