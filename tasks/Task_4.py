import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Saravana@123",
    database="HMBank"
)

cursor = conn.cursor()

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

cursor.close()
conn.close()
