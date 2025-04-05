import mysql.connector
from dao.banking_interface import BankingInterface
from exception.exceptions import InsufficientBalanceException

class BankingImpl(BankingInterface):
    def __init__(self, conn):
        self.conn = conn

    def create_customer(self, customer):
        cur = self.conn.cursor()
        cur.execute("""INSERT INTO Customers 
                       (customer_id, first_name, last_name, DOB, email, phone_number, perm_address) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s)""", (
            customer.customer_id, customer.first_name, customer.last_name,
            customer.dob, customer.email, customer.phone_number, customer.perm_address
        ))
        self.conn.commit()

    def create_account(self, account):
        cur = self.conn.cursor()
        cur.execute("""INSERT INTO Accounts 
                       (account_id, customer_id, account_type, balance) 
                       VALUES (%s, %s, %s, %s)""", (
            account.account_id, account.customer_id, account.account_type, account.balance
        ))
        self.conn.commit()

    def deposit(self, transaction):
        cur = self.conn.cursor()
        cur.execute("""INSERT INTO Transactions 
                       (transaction_id, account_id, transaction_type, amount, transaction_date) 
                       VALUES (%s, %s, %s, %s, %s)""", (
            transaction.transaction_id, transaction.account_id,
            transaction.transaction_type, transaction.amount, transaction.transaction_date
        ))
        cur.execute("UPDATE Accounts SET balance = balance + %s WHERE account_id = %s",
                    (transaction.amount, transaction.account_id))
        self.conn.commit()

    def withdraw(self, transaction):
        cur = self.conn.cursor()
        cur.execute("SELECT balance FROM Accounts WHERE account_id = %s", (transaction.account_id,))
        balance = cur.fetchone()[0]
        if transaction.amount > balance:
            raise InsufficientBalanceException("Not enough balance.")
        cur.execute("""INSERT INTO Transactions 
                       (transaction_id, account_id, transaction_type, amount, transaction_date) 
                       VALUES (%s, %s, %s, %s, %s)""", (
            transaction.transaction_id, transaction.account_id,
            transaction.transaction_type, transaction.amount, transaction.transaction_date
        ))
        cur.execute("UPDATE Accounts SET balance = balance - %s WHERE account_id = %s",
                    (transaction.amount, transaction.account_id))
        self.conn.commit()

    def view_balance(self, account_id):
        cur = self.conn.cursor()
        cur.execute("SELECT balance FROM Accounts WHERE account_id = %s", (account_id,))
        result = cur.fetchone()
        return result[0] if result else None
