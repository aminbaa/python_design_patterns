import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'(x: {self.x:.2f}, y: {self.y:.2f})'

    class PointFactory:

        def new_cartesian_point(self, x, y):
            p = Point()
            p.x, p.y = x, y
            return p

        def new_polar_point(self, rho, theta):
            x = rho * math.cos(theta)
            y = rho * math.sin(theta)
            p = Point()
            p.x, p.y = x, y
            return p

    factory = PointFactory()


if __name__ == '__main__':
    p1 = Point(2, 3)
    print(p1)
    p2 = Point.PointFactory().new_cartesian_point(2, 3)
    print(p2)
    p3 = Point.factory.new_polar_point(10, 3.14)
    print(p3)


