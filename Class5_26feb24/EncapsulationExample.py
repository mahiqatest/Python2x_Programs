class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_interest = 100

    # Access modifiers in python define as follows for public data members or methods normally define where
    # for protected declare with _protectedvar and private declare as __privatevar same applies to methods.
    # we can access protected and private variables through methods


    def public_fun(self):
        print(self.__private_interest)

    def deposit(self, amount):
        self.balance += amount

    def _withdraw(self, amount):
        self.balance -= amount

    def __show_balance(self):
        print("your balance in bank : ", self.balance)

    def if_auth_user(self, flag):  # if flag true then it will show balance
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")

    def bank_manager_cando_withdraw(self, amount):
        self._withdraw(amount)


jp_chase = BankAccount()
jp_chase.deposit(1000)
jp_chase.bank_manager_cando_withdraw(499)
jp_chase.if_auth_user(True)
jp_chase.public_fun()
