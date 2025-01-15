
class Account:
    def __init__(self, balance):
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative.")


account = Account(1000)


print("Current balance:", account.get_balance())
account.set_balance(2000)
print("Updated balance:", account.get_balance())
