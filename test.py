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