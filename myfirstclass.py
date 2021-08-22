class Person(object):
    # constructor (__new__)
    def __init__(self, name , age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        print(f"{self.name} is walking.")

    def run(self):
        print(f"{self.name} is running.")


john = Person("John", 28, 'male')
taro = Person("Taro", 18, 'male')
emma = Person("Emma", 40, 'female')

# インスタンス変数
# 「.」に続けてアクセス可能
print(john.name)
print(f"変更前{john.age}")
print(john.gender)
john.age = 29
print(f"変更後{john.age}")

print(taro.name)
print(taro.age)
print(taro.gender)

# インスタンスメソッド
john.walk()
emma.walk()
john.run()