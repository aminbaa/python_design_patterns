from enum import Enum
import math


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * math.cos(b)
    #         self.y = a * math.sin(b)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        x = rho * math.cos(theta)
        y = rho * math.sin(theta)
        return Point(x, y)

    def __str__(self):
        return f'(x: {self.x:.2f}, y: {self.y:.2f})'


if __name__ == '__main__':
    p1 = Point(2, 3)
    print(p1)
    p2 = Point.new_cartesian_point(2, 3)
    print(p2)
    p3 = Point.new_polar_point(10, 3.14)
    print(p3)


