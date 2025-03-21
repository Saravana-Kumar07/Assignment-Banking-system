# Assignment-Banking-system
## Task 1: Database creation
1. Create the database named "HMBank"
```sql
 CREATE DATABASE HMBank;
 USE HMBank;
 ```
 <img src="./outputs/o1.png" width="400" />

 2. Define the schema for the Customers, Accounts, and Transactions tables based on the provided schema.
- Customers Table:
    - `customer_id`: A unique ID for each customer (used as the primary key).
    - `first_name`: The customer's first name (text).
    - `last_name`: The customer's last name (text).
    - `DOB`:  The customer's date of birth.
    - `email`: The customer's email address (text).
    - `phone_number`: The customer's 10-digit phone number. It must be exactly 10 digits.
    - `perm_address`: The customer's permanent address (text).

- Accounts Table:
    - `account_id`: A unique ID for each account (used as the primary key).
    - `customer_id`: The ID of the customer who owns the account. This links to the customer_id in the Customers Table.
    - `account_type`:The type of account, like "Savings" or "Current" (text).
    - `balance`: The amount of money in the account. Starts at 0 by default and cannot be negative.

- Transactions Table
    - `transaction_id`:A unique ID for each transaction (used as the primary key).
    - `account_id`: The ID of the account involved in the transaction. This links to the account_id in the Accounts Table.
    - `transaction_type`: The type of transaction, like "Deposit" or "Withdrawal" (text).
    - `amount`: The amount of money involved in the transaction. It must be a positive number and cannot be null.
    - `transaction_date`:The date when the transaction happened.

3. Create an ERD (Entity Relationship Diagram) for the database.
    <img src="./outputs/erd.png" width="600" />

4. Create appropriate Primary Key and Foreign Key constraints for referential integrity.
- Primary Keys:
    - Customers: `customer_id`
    - Accounts: `account_id`
    - Transactions: `transaction_id`

- Foreign Keys:
    - Accounts references Customers: `customer_id`
    - Transactions references Accounts: `account_id`

6. Write SQL scripts to create the mentioned tables with appropriate data types, constraints, 
and relationships.   
• Customers  
• Accounts 
• Transactions 

```sql
CREATE TABLE Customers(
    -> customer_id INT,
    -> first_name VARCHAR(200),
    -> last_name VARCHAR(200),
    -> DOB DATE,
    -> email VARCHAR(200),
    -> phone_number INT CHECK (CHAR_LENGTH(phone_number) = 10),
    ->  perm_address VARCHAR(200),
    -> PRIMARY KEY (customer_id)
    -> );
```
<img src="./outputs/o2.png" width="400" />
    