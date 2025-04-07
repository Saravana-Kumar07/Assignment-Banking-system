# <p align='center'> Assignment Banking system - Python tasks</p>
### Name: Saravana Kumar S
Superset ID: 5371342<br>
College: Saveetha Engineering college

## Task 1: Conditional Statements
In a bank, you have been given the task is to create a program that checks if a customer is eligible for 
a loan based on their credit score and income. The eligibility criteria are as follows: 
• Credit Score must be above 700. 
• Annual Income must be at least $50,000. 
Tasks: 
1. Write a program that takes the customer's credit score and annual income as input. 
2. Use conditional statements (if-else) to determine if the customer is eligible for a loan. 
3. Display an appropriate message based on eligibility.
```py
credit_score = int(input("Enter ypur credit score: "))
annual_income = int(input("Enter your annual income: "))

if credit_score > 700 and annual_income >= 50_000:
    print("You are eligible for a loan ")
else:
    print("You are not eligible for a loan ")
 ```
 <img src="./outputs/p1.png" width="350" />

## Task 2: Nested Conditional Statements 
Create a program that simulates an ATM transaction. Display options such as "Check Balance," 
"Withdraw," "Deposit,". Ask the user to enter their current balance and the amount they want to 
withdraw or deposit. Implement checks to ensure that the withdrawal amount is not greater than the 
available balance and that the withdrawal amount is in multiples of 100 or 500. Display appropriate 
messages for success or failure.
```py
curr_bal = int(input("Enter your current balance: "))
while True:
    print(
        "Choose what you would like to do\n"
        "1. check balance\n"
        "2. withdrawl\n"
        "3. deposit\n"
        "4. Exit")
    ask  = int(input("Enter a value: "))

    if ask == 1:
        print(f"Your current balance is ${curr_bal}\n")
    elif ask == 2:
        amt = int(input("Enter amount to withdraw: "))
        if amt <= curr_bal and amt%100 == 0:
            curr_bal -= amt
            print("Transaction Successful!!\n")
        elif amt > curr_bal:
            print("Insufficient Balance!!\n")
        else:
            print("Enter amount in multiples of 100 or 500\n")
    elif ask == 3:
        amt = int(input("Enter amount to be deposited: "))
        curr_bal += amt
        print("Transaction Successful!!")
        print(f"Current balance: {curr_bal}\n")
    elif ask == 4:
        break
    else:
        print("Please enter a valid value\n")
 ```
 <img src="./outputs/p2.png" width="350" />

 ## Task 3: Loop Structures 
You are responsible for calculating compound interest on savings accounts for bank customers. You 
need to calculate the future balance for each customer's savings account after a certain number of years. 
Tasks: 
1. Create a program that calculates the future balance of a savings account. 
2. Use a loop structure (e.g., for loop) to calculate the balance for multiple customers. 
3. Prompt the user to enter the initial balance, annual interest rate, and the number of years. 
4. Calculate the future balance using the formula:      
future_balance = initial_balance * (1 + annual_interest_rate/100)^years. 
5. Display the future balance for each customer. 
```py
initial_balance = int(input("Enter initial balance: "))
annual_interest_rate = int(input("Enter annual interest rate: "))
number_of_years = int(input("Enter number of years: "))

future_balance = round(initial_balance * (1 + annual_interest_rate/100)**number_of_years,2)

print(f"Your balance after {number_of_years} year will be {future_balance}")
 ```
 <img src="./outputs/p3.png" width="350" />

## Task 4: Looping, Array and Data Validation 
You are tasked with creating a program that allows bank customers to check their account balances. 
The program should handle multiple customer accounts, and the customer should be able to enter their 
account number, balance to check the balance. 
Tasks: 
1. Create a Python program that simulates a bank with multiple customer accounts. 
2. Use a loop (e.g., while loop) to repeatedly ask the user for their account number and 
balance until they enter a valid account number. 
3. Validate the account number entered by the user. 
4. If the account number is valid, display the account balance. If not, ask the user to try again.

```py
while True:
    try:
        account = int(input("Enter your account number: "))

        cursor.execute("SELECT balance FROM Accounts WHERE account_id = %s", (account,))
        result = cursor.fetchone()

        if result:
            print(f"Available balance: {result[0]}")
            break
        else:
            print("Enter a valid account number...\n")

    except ValueError:
        print("Please enter a valid numeric account number.")
```
 <img src="./outputs/p4.png" width="250" />

 ## Task 5: Password Validation 
Write a program that prompts the user to create a password for their bank account. Implement if 
conditions to validate the password according to these rules: 
• The password must be at least 8 characters long. 
• It must contain at least one uppercase letter. 
• It must contain at least one digit. 
• Display appropriate messages to indicate whether their password is valid or not.

```py
def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."

    return True, "Password is valid."
while True:
    password = input("Create a password for your bank account: ")
    is_valid, message = validate_password(password)
    if is_valid:
        print(message, "\nYour password has been created successfully!!")
        break
    else:
        print("Invalid password.\n" + message + "\n")
```
 <img src="./outputs/p5.png" width="400" />

 ## Task 6: Transactions
Create a program that maintains a list of bank transactions (deposits and withdrawals) for a customer. 
Use a while loop to allow the user to keep adding transactions until they choose to exit. Display the 
transaction history upon exit using looping statements.
```py
account = int(input("Enter account number: "))

print(f"Transaction history for account no. {account} :")

query = """
    SELECT amount, transaction_type, transaction_date 
    FROM Transactions 
    WHERE account_id = %s
    ORDER BY transaction_date DESC
"""
cursor.execute(query, (account,))
rows = cursor.fetchall()

if rows:
    headers = ["Amount", "Transaction Type", "Transaction Date"]
    print(tabulate(rows, headers=headers, tablefmt="psql"))
else:
    print("No transactions found for this account.")
```
<img src="./outputs/p6.png" width="400" />

## Test.py:
```py
from entity.customer import Customer
from entity.account import Account
from entity.transaction import Transaction
from dao.banking_impl import BankingImpl
from util.dbproperty import get_connection_props
from util.db_connection import get_connection
from datetime import datetime

conn_str = get_connection_props("util/db.properties")
conn = get_connection(conn_str)
banking = BankingImpl(conn)

def main():
    while True:
        print("\n===== Banking System Menu =====")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. View Balance")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer = Customer(
                int(input("Customer ID: ")),
                input("First Name: "),
                input("Last Name: "),
                input("DOB (YYYY-MM-DD): "),
                input("Email: "),
                input("Phone Number: "),
                input("Permanent Address: ")
            )
            banking.create_customer(customer)

        elif choice == '2':
            account = Account(
                int(input("Account ID: ")),
                int(input("Customer ID: ")),
                input("Account Type: "),
                int(input("Initial Balance: "))
            )
            banking.create_account(account)

        elif choice == '3':
            transaction = Transaction(
                int(input("Transaction ID: ")),
                int(input("Account ID: ")),
                "deposit",
                int(input("Amount to Deposit: ")),
                datetime.now().date()
            )
            banking.deposit(transaction)

        elif choice == '4':
            transaction = Transaction(
                int(input("Transaction ID: ")),
                int(input("Account ID: ")),
                "withdraw",
                int(input("Amount to Withdraw: ")),
                datetime.now().date()
            )
            try:
                banking.withdraw(transaction)
            except Exception as e:
                print(e)

        elif choice == '5':
            acc_id = int(input("Enter Account ID: "))
            print("Current Balance:", banking.view_balance(acc_id))

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid option!")

main()
```
## Task 7: Class & Object 
1. Create a `Customer` class with the following confidential attributes
<img src="./outputs/p7.png" width="400" />
<img src="./outputs/p8.png" width="400" />
2. Create an `Account` class with the following confidential attributes
<img src="./outputs/p10.png" width="400" />
<img src="./outputs/p9.png" width="400" />

## Main.py:
```py
from dao.BankServiceProviderImpl import BankServiceProviderImpl
from entity.Customer1 import Customer

class BankApp:
    @staticmethod
    def start():
        bank = BankServiceProviderImpl("Hexaware Bank", "123 Chennai")
        
        while True:
            print("\nWelcome to the bank!")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Account Details")
            print("6. List Accounts")
            print("7. Calculate Interest")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                acc_type = input("Enter account type (Savings, Current, ZeroBalance): ")
                customer_id = input("Enter customer ID: ")
                customer_name = input("Enter customer name: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                address = input("Enter address: ")
                balance = float(input("Enter initial balance: "))
                accNo = input("Enter account number: ")
                customer = Customer(customer_id, *customer_name.split(), email, phone_number, address)
                account = bank.create_account(customer, acc_type, accNo, balance)

                if account:
                    print(f"Account created successfully. Account number: {account.account_number}")

            elif choice == "2":
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter amount to deposit: "))
                balance = bank.deposit(account_number, amount)
                if balance is not None:
                    print(f"Deposit successful. New balance: {balance}")

            elif choice == "3":
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter amount to withdraw: "))
                balance = bank.withdraw(account_number, amount)
                if balance is not None:
                    print(f"Withdrawal successful. New balance: {balance}")

            elif choice == "4":
                from_account_number = int(input("Enter source account number: "))
                to_account_number = int(input("Enter destination account number: "))
                amount = float(input("Enter amount to transfer: "))
                balance = bank.transfer(from_account_number, to_account_number, amount)
                if balance is not None:
                    print(f"Transfer successful. New balance: {balance}")

            elif choice == "5":
                account_number = int(input("Enter account number: "))
                account_details = bank.get_account_details(account_number)
                if account_details:
                    print("Account details:")
                    print(f"Account Number: {account_details.account_number}")
                    print(f"Account Type: {account_details.account_type}")
                    print(f"Account Balance: {account_details.account_balance}")
                    print(f"Customer: {account_details.customer.first_name} {account_details.customer.last_name}")
                    print(f"Customer ID: {account_details.customer.customer_id}")
                    print(f"Customer Email: {account_details.customer.email}")
                    print(f"Customer Phone Number: {account_details.customer.phone_number}")
                    print(f"Customer Address: {account_details.customer.address}")

            elif choice == "6":
                accounts = bank.list_accounts()
                if accounts:
                    print("List of accounts:")
                    for acc in accounts:
                        print(f"Account Number: {acc.account_number}, Type: {acc.account_type}, Balance: {acc.account_balance}")

            elif choice == "7":
                bank.calculate_interest()

            elif choice == "8":
                print("Exiting...")
                break

            else:
                print("Invalid choice.")

BankApp.start()
```

## BankServiceProviderImpl.py:
```py
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
```

## IBankServiceProvider(abstarct class):
```py
from abc import ABC, abstractmethod
class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer, accNo, accType, balance):
        pass
    
    @abstractmethod
    def list_accounts(self):
        pass
    
    @abstractmethod
    def calculate_interest(self):
        pass
```
## CustomerServiceProviderImpl.py:
```py
class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].account_balance
        else:
            print("Account not found.")
            return None
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].account_balance += amount
            return self.accounts[account_number].account_balance
        else:
            print("Account not found.")
            return None
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.account_balance >= amount:
                account.account_balance -= amount
                return account.account_balance
            else:
                print("Insufficient funds.")
                return None
        else:
            print("Account not found.")
            return None
    
    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            from_account = self.accounts[from_account_number]
            to_account = self.accounts[to_account_number]
            if from_account.account_balance >= amount:
                from_account.account_balance -= amount
                to_account.account_balance += amount
                return from_account.account_balance
            else:
                print("Insufficient funds.")
                return None
        else:
            print("One or both accounts not found.")
            return None
    
    def get_account_details(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            return account
        else:
            print("Account not found.")
            return None
```

## ICustomerServiceProvider.py(abstarct class):
```py
from abc import ABC, abstractmethod

class ICustomerServiceProvider(ABC):
    @abstractmethod
    def get_account_balance(self, account_number):
        pass
    
    @abstractmethod
    def deposit(self, account_number, amount):
        pass
    
    @abstractmethod
    def withdraw(self, account_number, amount):
        pass
    
    @abstractmethod
    def transfer(self, from_account_number, to_account_number, amount):
        pass
    
    @abstractmethod
    def get_account_details(self, account_number):
        pass
```

## Savings account.py:
```py
class SavingsAccount(Account):
    def __init__(self, customer, interest_rate, account_balance=500):
        super().__init__("Savings", account_balance, customer)
        self.interest_rate = interest_rate
```

## Zero balance.py:
```py
class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__("Zero Balance", 0, customer)
```

## CurrentAccount.py:
```py
class CurrentAccount(Account):
    def __init__(self, customer, overdraft_limit, account_balance):
        super().__init__("Current", account_balance, customer)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.account_balance + self.overdraft_limit:
            print("Insufficient funds!")
        else:
            self.account_balance -= amount
            print("Withdrawal successful!")
```
