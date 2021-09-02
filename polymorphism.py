class MyClass:
    def __str__(self):
        return "MyClassの__str__"
    # pass

def printvalue(arg):
    print(arg + 1)

printvalue(True)


# mc = MyClass()
# print(mc)  # mc.__str__()
# print(1)  # 1.__str__()
# print("1")  # "1".__str__()
# print(True)  # True.__str__()
# print([1, 2, 3])  # [1, 2, 3].__str__()

various_types = [1, "1", True, [1, 2, 3], (1,), {'1', 1}, {1}]
for elem in various_types:
    print(elem)
