
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance *= (1 + self.interest_rate)
    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print("Insufficient funds")



class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.overdraft_limit = 5000

    def withdraw(self, amount):
        if self.balance - amount > -self.overdraft_limit:
            self.balance -= amount
        else:
            print("Insufficient funds")


def main():
    savings = SavingsAccount(123, 1000, 0.01)
    savings.deposit(100)
    savings.withdraw(200)
    savings.add_interest()
    print(savings.balance)

    checking = CheckingAccount(456, 1000)
    checking.deposit(100)
    checking.withdraw(200)
    checking.withdraw(2000)
    print(checking.balance)

if __name__ == "__main__":
    main()

