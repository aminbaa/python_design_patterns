from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# OCP = Open for extension, Closed for modification

class ProductFilter:  # WARNING: Violates Open-Close-Principle
    @staticmethod
    def filter_by_color(products, color):
        for p in products:
            if p.color == color:
                yield p

    @staticmethod
    def filter_by_size(products, size):
        for p in products:
            if p.size == size:
                yield p

    @staticmethod
    def filter_by_size_and_color(products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p

    @staticmethod
    def filter_by_size_or_color(products, size, color):
        for p in products:
            if p.size == size or p.color == color:
                yield p


# Specification pattern

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(
            map(lambda spec: spec.is_satisfied(item), self.args)
        )


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product(name='Apple', color=Color.GREEN, size=Size.SMALL)
    tree = Product(name='Tree', color=Color.GREEN, size=Size.LARGE)
    house = Product(name='House', color=Color.BLUE, size=Size.LARGE)

    sample_products = [apple, tree, house]

    pf = ProductFilter()

    print('Green Products (old approach):')

    for p in pf.filter_by_color(sample_products, color=Color.GREEN):
        print(f'Name: {p.name}, Color: {p.color}, Size: {p.size}')

    bf = BetterFilter()

    print('Green Products (better approach):')
    is_green = ColorSpecification(Color.GREEN)
    for p in bf.filter(sample_products, is_green):
        print(f'Name: {p.name}, Color: {p.color}, Size: {p.size}')

    print('Large Products (better approach):')
    is_large = SizeSpecification(Size.LARGE)
    for p in bf.filter(sample_products, is_large):
        print(f'Name: {p.name}, Color: {p.color}, Size: {p.size}')

    print('Large and BLue Products (better approach):')
    is_large = SizeSpecification(size=Size.LARGE)
    is_blue = ColorSpecification(color=Color.BLUE)

    is_large_and_blue_1 = AndSpecification(is_large, is_blue)
    for p in bf.filter(sample_products, is_large_and_blue_1):
        print(f'Name: {p.name}, Color: {p.color}, Size: {p.size}')

    is_large_and_blue_2 = is_large & is_blue
    for p in bf.filter(sample_products, is_large_and_blue_2):
        print(f'Name: {p.name}, Color: {p.color}, Size: {p.size}')




