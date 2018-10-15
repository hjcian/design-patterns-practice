class Prototype(object):
    value = 'default' # a global attribute for Prototype instance
    def clone(self, **kwargs):
        obj = self.__class__()
        obj.__dict__.update(kwargs)
        return obj

class Register(object):
    def __init__(self):
        self._objects = {}
    
    def register_object(self, name, obj):
        self._objects[name] = obj
    
    def get_objects(self):
        return self._objects

if __name__ == "__main__":
    register = Register()
    prototyper = Prototype()
    a = prototyper.clone() # default object with only one attribute: value='default'
    b = prototyper.clone(value=123, id='007')
    c = prototyper.clone(value=456, uuid='ASDFG98765')
    register.register_object('obj_a', a)
    register.register_object('obj_b', b)
    register.register_object('obj_c', c)
    print(type(a))
    print(type(b))
    print(type(c))
    print([(name, o.value) for name, o in register.get_objects().items()])

