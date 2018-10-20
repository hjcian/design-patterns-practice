class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "bark"

class Cat(object):
    def __init__(self):
        self.name = "Cat"
    def meow(self):
        return "Meow"

class Adapter(object):
    def __init__(self, obj, **adapted_methods):
        self._obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        print("not found {}, use object's attr.".format(attr))
        return getattr(self._obj, attr) # 此法安全地調用attr，若沒有此attr就報錯
        # return self._obj.__getattribute__(attr) # 此法同樣安全地調用attr，若沒有此attr就報錯
        # return self._obj_.__getattr__(attr) # 此法會產生無窮迴圈，因為__getattr__(attr)支援的行為就是在__dict__中找不到attr時調用，故造成無窮迴圈

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__

def main():
    objects = []
    dog = Dog()
    cat = Cat()
    objects.append(Adapter(dog, make_noise=dog.bark))
    objects.append(Adapter(cat, make_noise=cat.meow))
    # 運用__dict__都方法動態產生屬性並將舊class重新用新的屬性名稱包裝
    for o in objects:
        print("{} goes {}".format(o.name, o.make_noise()))
        print(o.x)
        # o.name會在Adapter中找不到，所以寫一個__getattr__去攔截屬性訪問，引導到原物件的屬性
        

if __name__ == "__main__":
    main()

