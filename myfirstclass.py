class Person(object):
    # constructor (__new__)
    def __init__(self, name , age, gender):
        self.name = name
        self.age = age
        self.gender = gender


john = Person("John", 28, 'male')
taro = Person("Taro", 18, 'male')
emma = Person("Emma", 40, 'female')

print(john.name)
print(john.age)
print(john.gender)
