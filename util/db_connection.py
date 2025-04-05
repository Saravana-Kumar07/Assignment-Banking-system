import mysql.connector

def get_connection(props):
    return mysql.connector.connect(
        host=props["host"],
        user=props["user"],
        password=props["password"],
        database=props["database"]
    )
