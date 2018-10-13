import random

class PetShop(object):
    # PetShop is abstract factory
    def __init__(self, pet_factory=None):
        self.pet_factory = pet_factory # instantiation
    
    def show_pet(self):
        pet = self.pet_factory
        print("We have a {}".format(pet))
        print("It says: '{}'".format(pet.speak()))

class Dog(object):
    def speak(self):
        return "Woof"
    
    def __str__(self):
        return "DOG"

class Cat(object):
    def speak(self):
        return "Meow"

    def __str__(self):
        return "CAT"

# Additional factories:
# Create a random animal
def random_animal():
    """Let's be dynamic!"""
    return random.choice([Dog, Cat])() #use () return an object directly

if __name__ == "__main__":
    cat = Cat()
    pet = PetShop(cat)
    pet.show_pet()

    for i in range(3):
        pet = PetShop(random_animal())
        pet.show_pet()
        print("==========")