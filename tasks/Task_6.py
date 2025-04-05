import mysql.connector
from tabulate import tabulate
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Saravana@123",
    database="HMBank"
)

cursor = conn.cursor()

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

cursor.close()
conn.close()
