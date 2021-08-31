class Animal(object):
    def __init__(self, name):
        self.name = name
        print("Animal init is called.")

    def breath(self):
        print(f"{self.name} is breathing.")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Bird(Animal):
    pass

pochi = Dog("pochi")
tama = Cat("tama")
print(pochi.name)
print(tama.name)
pochi.breath()
tama.breath()