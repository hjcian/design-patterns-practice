class Dog(object):
    def speak(self):
        return "Woof"

class Cat(object):
    def speak(self):
        return "Meow"

# factory 
def getAnimal(animal_type='cat'):
    animal_enum = {
        "cat": Cat,
        "dog": Dog,
    }
    return animal_enum[animal_type]()

if __name__ == "__main__":
    cat = getAnimal("cat")
    print(cat.speak())

    dog = getAnimal("dog")
    print(dog.speak())