class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = amount + self.balance
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

toby = BankAccount("Bimbo", 15000)

print(toby.owner)
print(toby.balance)
print(toby.deposit(15000))
print(toby.withdraw(7000))