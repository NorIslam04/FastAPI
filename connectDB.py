import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="islam"
    )
    if connection.is_connected():
        print("Connected to MySQL successfully!")
        connection.close()
except Error as e:
    print(f"Error: {e}")
