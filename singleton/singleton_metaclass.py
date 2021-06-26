class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    def __init__(self):
        print("Initializing MyClass")


if __name__ == '__main__':
    ins1 = MyClass()
    ins2 = MyClass()

    print(ins1 == ins2)

