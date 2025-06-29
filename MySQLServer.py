# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

# Database configuration
# IMPORTANT: Replace with your MySQL server credentials
DB_CONFIG = {
    'host': 'localhost',  
    'user': 'localhost',
    'password': '17October1970$$' 
}

DATABASE_NAME = 'alx_book_store'

def create_database():
    """
    Connects to MySQL server and creates the specified database.
    Does not fail if the database already exists.
    Handles connection errors and ensures proper closing.
    """
    connection = None
    cursor = None
    try:
        # Establish a connection to the MySQL server
        # We don't specify a database here, as we intend to create one
        print(f"Attempting to connect to MySQL server at {DB_CONFIG['host']}...")
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Create the database using IF NOT EXISTS to prevent errors if it already exists
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
        cursor.execute(create_db_query)

        print(f"Database '{DATABASE_NAME}' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist (this shouldn't happen during creation).")
        else:
            print(f"Error connecting to the database or creating it: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure cursor and connection are closed
        if cursor:
            cursor.close()
            print("Cursor closed.")
        if connection and connection.is_connected():
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    create_database()