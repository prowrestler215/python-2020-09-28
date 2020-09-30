class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        print('Running the __init__!')
        # return self

    def deposit(self, amount_to_deposit):
        print(f'Depositing {amount_to_deposit}')
        # self.balance += amount_to_deposit
        self.balance = self.balance + amount_to_deposit
        return self

    def withdraw(self, amount_to_withdraw):
        print(f'Withdrawing {amount_to_withdraw}')
        if self.balance < amount_to_withdraw:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            # self.balance += amount_to_withdraw
            self.balance = self.balance - amount_to_withdraw
        return self

    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self

    def yield_interest(self):
        # check if the account balance is positive
        if self.balance > 0:
            # yield interest
            # self.balance += self.balance * self.int_rate
            print('Yielding interest!')
            self.balance = self.balance + (self.balance * self.int_rate)
        else:
            print('Not enough balance for interest!')
        return self


default = BankAccount(2, 1000)
print(default)
print(default.balance)
print(default.int_rate)
# checking = BankAccount(0.01, 500)
# print(checking)
# savings = BankAccount(0.02, 150)

# checking.deposit(10).deposit(50).deposit(5).withdraw(100).display_account_info() # 465
# savings.deposit(500).deposit(10).withdraw(100).withdraw(100).withdraw(100).withdraw(100).display_account_info() # 260

# savings.withdraw(300).display_account_info()

# savings.withdraw(255).withdraw(1).display_account_info()

# def return_default():
#     print('returning default!')
#     return '1'

# return_value = return_default()
# print(return_value)
