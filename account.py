class Account(object):

    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        Account.count += 1

    def withdraw(self, amount):
        if amount <= self.balance:
            # self.balance = self.balance - amount
            self.balance -= amount
            self.show_balance()
            # print(f"self.balance: {self.balance}")
        else:
            print(f"残高({self.balance}円)が足りません")


    def deposit(self, amount):
        self.balance += amount
        # print(f"self.balance: {self.balance}")
        self.show_balance()

    def show_balance(self):
        # print(f"{self.name}の残高は{self.balance}円です")
        print("{0.name}(口座番号: {0.account_number})の残高は{0.balance}円です".format(self))



myaccount = Account(name="my account", balance=1000)
print(myaccount.name)
print(myaccount.balance)
myaccount.withdraw(300)
myaccount.deposit(500)
myaccount.withdraw(1500)
youraccount = Account(name="your account", balance=10000)
youraccount.deposit(5000)