class MyClass:

    def mymethod(self):
        print("This is normal method from {}.".format(self))

    @staticmethod
    def mystaticmethod():
        print("This is staticmethod!")


c = MyClass()
c.mymethod()
MyClass.mystaticmethod()
# c.mystaticmethod()