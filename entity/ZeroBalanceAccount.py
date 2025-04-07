from entity.Account1 import Account
class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__("Zero Balance", 0, customer)