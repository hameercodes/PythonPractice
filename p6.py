#Create a BankAccount class with methods deposit, withdraw, and get_balance.
class BankAccount:
    def __init__(self,balance,account):
        self.balance = balance
        self.account = account

    def deposit(self, account, amount):
        if(self.account == account):
            self.balance += amount
        print(f"Your account {self.account} has been credited to NRP.{amount}. Your new balance is NRP.{self.balance}.")
    
    def withdraw(self, account, amount):
        if(self.account == account):
            self.balance -= amount
        print(f"NRP.{amount} has been withdrawn from your account {self.account}. Your new balance is NRP.{self.balance}")

    def get_balance(self, account):
        if(self.account == account):
            print(f"Your current balance is NRP.{self.balance}.")

c1 = BankAccount(10000, 1234)
c1.deposit(1234, 500)
c1.withdraw(1234,1000)
c1.get_balance(1234)
c2 = BankAccount(40000, 1235)
c2.deposit(1235, 5000)
c2.withdraw(1235,10000)
c2.get_balance(1235)