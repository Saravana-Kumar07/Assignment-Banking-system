from abc import ABC, abstractmethod
from entity.customer import Customer
from entity.account import Account
from entity.transaction import Transaction

class BankingInterface(ABC):

    @abstractmethod
    def create_customer(self, customer: Customer):
        pass

    @abstractmethod
    def create_account(self, account: Account):
        pass

    @abstractmethod
    def deposit(self, transaction: Transaction):
        pass

    @abstractmethod
    def withdraw(self, transaction: Transaction):
        pass

    @abstractmethod
    def view_balance(self, account_id: int) -> int:
        pass
