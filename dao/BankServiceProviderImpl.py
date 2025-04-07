from dao.CustomerServiceProviderImpl import CustomerServiceProviderImpl
from dao.IBankServiceProvider import IBankServiceProvider
from entity.Account1 import Account
from entity.CurrentAccount import CurrentAccount
from entity.SavingsAccount import SavingsAccount
from entity.ZeroBalanceAccount import ZeroBalanceAccount

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider,Account):
    def __init__(self, branch_name, branch_address):
        super().__init__()
        self.branch_name = branch_name
        self.branch_address = branch_address

    def create_account(self, customer, accNo, accType, balance):
        if accType == "Savings":
            account = SavingsAccount(customer, interest_rate=0.05, account_balance=balance)
        elif accType == "Current":
            account = CurrentAccount(customer, overdraft_limit=1000, account_balance=balance)
        elif accType == "ZeroBalance":
            account = ZeroBalanceAccount(customer)
        else:
            print("Invalid account type.")
            return None
        
        self.accounts[accNo] = account
        return account
    
    def list_accounts(self):
        return list(self.accounts.values())
    
    def calculate_interest(self):
        for acc in self.accounts.values():
            if isinstance(acc, SavingsAccount):
                interest = acc.account_balance * acc.interest_rate
                print(f"Interest for account {acc.account_number}: {interest}")