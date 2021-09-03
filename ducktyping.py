class Duck:
    """
    This is a class for Duck.

    Attributes:
        name (str): the name of duck

    Method:
        walk: print ***
        quack: print ***
        fly: print ***
    """
    def __init__(self, name):
        """
        The constructor for Duck class
        :param name: the name of the duck
        """
        self.name = name

    def walk(self):
        print("walking...")

    def quack(self):
        print("quack quack...!")

    def fly(self):
        print("Whee!!")


class Penguin:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking...")

    def quack(self):
        print("quack quack...??")

    def swim(self):
        print("Swimming!")


def walk_and_quack(duck):
    print(f"I'm {duck.name}.")
    duck.walk()
    duck.quack()


if __name__ == "__main__":
    # print(help(Duck))
    print(help(Duck.__init__))
    print(help(Duck.__doc__))
    print(Duck.__init__.__doc__)
    donald = Duck("Donald")
    scrooge = Duck("Scrooge")
    daisy = Duck("Daisy")
    pingu = Penguin("Pingu")
    # donald.walk()
    # donald.quack()
    # pingu.walk()
    # pingu.quack()
    # walk_and_quack(donald)
    # walk_and_quack(pingu)
    duck_list = [donald, pingu, scrooge, daisy]
    for duck in duck_list:
        walk_and_quack(duck)