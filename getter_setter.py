class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        print("get_age called!")
        return self._age

    @age.setter
    def age(self, age):
        print("set_age called!")
        if age < 0:
            print("0以上の値を入れてください")
        else:
            self._age

    # age = property(get_age, set_age)

john = Person("John", 10)
print(john.age)
john.age = -10
john.age = 15
print(john.age)

# print(john.age)
# print(john.get_age())
# john.age = 15
# john.set_age(-20)
# print(john.age)
# print(john.get_age())