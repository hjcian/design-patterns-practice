class Building(object):
    def __init__(self):
        self.build_floor()
        self.build_size()
    
    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotADirectoryError

    def __repr__(self):
        return "Building: {0.floor} {0.size}".format(self)

class House(Building):
    def build_floor(self):
        self.floor = "two"
    
    def build_size(self):
        self.size = "huge"

class Flat(Building):
    def build_floor(self):
        self.floor = "one"
    
    def build_size(self):
        self.size = "small"

class ComplexBuilding(object):
    def __repr__(self):
        return "ComplexBuilding: {0.floor} {0.size}".format(self)

class ComplexTower(ComplexBuilding):
    def build_floor(self):
        self.floor = "hundred"

    def build_size(self):
        self.size = "outer space"

def construct(cls):
    build = cls()
    build.build_floor()
    build.build_size()
    return build

if __name__ == "__main__":
    house = House()
    print(house)
    flat = Flat()
    print(flat)

    tower = construct(ComplexTower)
    print(tower)