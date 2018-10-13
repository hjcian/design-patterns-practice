class Borg(object):
    _shared_dict = {}    
    def __init__(self):
        self.__dict__ = self._shared_dict
        self.stat = None
    
    def __str__(self):
        return self.stat

class SubBorg(Borg):
    pass

class SingletonFactory(object):
    _instance = None
    def __init__(self):
        if SingletonFactory._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SingletonFactory._instance = self

    @staticmethod
    def getInst():
        if SingletonFactory._instance is None:
            SingletonFactory()
        return SingletonFactory._instance

class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """
    def __init__(self, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        self._instance = None
        print("__init__")

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        print("__call__")
        return self._instance


class MyClass(metaclass=Singleton):
    """
    Example class.
    """
    pass


if __name__ == "__main__":
    # a = Borg()
    # s = SingletonFactory()
    # print(s)
    # ss = SingletonFactory.getInst()
    # print(ss)
    
    a = MyClass()
    print(a)
    b = MyClass()
    print(b)
