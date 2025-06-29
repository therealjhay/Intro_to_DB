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

def create_alx_book_store_database():
    """
    Connects to the MySQL server and creates the 'alx_book_store' database.
    It won't fail if the database already exists.
    Handles connection errors and ensures proper closing of resources.
    """
    connection = None
    cursor = None
    try:
        # Attempt to connect to the MySQL server (without specifying a database initially)
        print(f"Attempting to connect to MySQL server at {DB_CONFIG['host']}...")
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Execute the SQL query to create the database IF NOT EXISTS
        # This prevents errors if 'alx_book_store' already exists
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
        cursor.execute(create_db_query)

        print(f"Database '{DATABASE_NAME}' created successfully!")

    except mysql.connector.Error as err:
        # Catch specific MySQL connection errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Double-check your MySQL username and password in the script.")
        else:
            print(f"An error occurred while connecting to MySQL or creating the database: {err}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        # Always ensure the cursor and connection are closed
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_alx_book_store_database()
