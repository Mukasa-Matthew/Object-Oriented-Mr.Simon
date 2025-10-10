
class ATM:
    def __init__(self, balance):
        self.balance = balance  

    def check_balance(self):
        print("Your balance is:", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient funds or invalid amount.")


# Example showing lack of encapsulation:
atm = ATM(500)
atm.check_balance()


atm.balance = 9999  # easily (and incorrectly) changed from outside!
print("After unauthorized balance change:")
atm.check_balance()
