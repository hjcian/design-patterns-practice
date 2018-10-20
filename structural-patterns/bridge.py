class ImplementA(object):
    def doSomething(self, x, y, radius):
        print("do A: ({}, {}): {} ".format(x, y, radius))

class ImplementB(object):
    def doSomething(self, x, y, radius):
        print("do B: ({}, {}): {} ".format(x, y, radius))

class Abstraction(object):
    def __init__(self, x, y, radius, obj):
        self.x = x
        self.y = y
        self.radius = radius
        self.obj = obj

    # low-level i.e. Implementation specific
    # 重新包裝方法名稱供呼叫
    def draw(self):
        self.obj.doSomething(self.x, self.y, self.radius)

    # high-level i.e. Abstraction specific
    # new interface提供的新方法，例如修改屬性
    def scale(self, scalar):
        self.radius *= scalar

def main():
    objects = [
        Abstraction(3, 4, 5, ImplementA()),
        Abstraction(8, 15, 17, ImplementB()),
    ]
    for o in objects:
        o.scale(3)
        o.draw()


if __name__ == "__main__":
    main()