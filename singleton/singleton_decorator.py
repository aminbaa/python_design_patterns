def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class MyClass:
    def __init__(self):
        print('Initializing MyClass')


if __name__ == '__main__':
    ins1 = MyClass()
    ins2 = MyClass()




