
class User:
    def __init__(self, name, money, bank_number):
        self.name = name
        self.money = money
        self.bank_number = bank_number

class ATM:
    def __init__(self, user, starting_money, deposit_money, withdraw_money, check_balance):
        self.user = user
        self.starting_money = starting_money
        self.deposit_money = deposit_money
        self.withdraw_money = withdraw_money
        self.check_balance = starting_money + deposit_money - withdraw_money



