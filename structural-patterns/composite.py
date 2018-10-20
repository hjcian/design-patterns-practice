class Component(object):
    def draw(self):
        raise NotImplementedError("Need implement this")

class Containee(Component):
    def __init__(self, name):
        self.name = name
    def draw(self):
        print("{} draw".format(self.name))

class Container(Component):
    def __init__(self, name):
        self.name = name
        self.bucket = set()
    
    def draw(self):
        print("I'm Container {}!".format(self.name))
        for cnt in self.bucket:
            cnt.draw()

    def addContainee(self, cnt):
        self.bucket.add(cnt)
    
    def delContainee(self, cnt):
        self.bucket.discard(cnt)

    
if __name__ == "__main__":
    a = Containee("a")
    b = Containee("b")
    c = Containee("c")
    A = Container("A")
    A.addContainee(a)
    A.addContainee(b)
    B = Container("B")
    B.addContainee(c)
    B.addContainee(A)
    B.draw()