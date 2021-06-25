# Liskov Substitution Principle

"""
The Liskov Substitution Principle in practical software development.
The principle defines that objects of a superclass shall be
replaceable with objects of its subclasses without breaking the application.
That requires the objects of your subclasses to behave in the same way as the objects of your superclass.
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def __str__(self):
        return f'width: {self.width}, height: {self.height}'


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected_area = int(w * 10)
    print(f'I expected an area of {expected_area}, got {rc.area}')
    print('---------------------------------')


rc_1 = Rectangle(2, 3)
use_it(rc_1)

sq = Square(5)
use_it(sq)
