import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (update user/password/host as needed)
        conn = mysql.connector.connect(
            host="localhost",
            user="localhost",
            password="17October1970$$"
        )

        cursor = conn.cursor()

        # Attempt to create database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Error creating database: {err}")

    except mysql.connector.Error as err:
        print(f"Failed to connect to the database server: {err}")
    finally:
        # Ensure connection is closed
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()
