class BankAccount:
    def __init__(self, balance):
        self.__balance = balance



    def get_balance(self):
        return self.__balance


    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount


    