class DataBase:
    _instance = None

    def __init__(self):
        print('initializing the class')

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    d1 = DataBase()
    d2 = DataBase()
    print(d1 == d2)
