#!/usr/bin/env python3
"""
Creates the 'alx_book_store' database in MySQL if it does not already exist.
"""

import mysql.connector
from mysql.connector import Error


def create_database():
    """Connect to MySQL and create alx_book_store database if missing."""
    connection = None
    cursor = None
    try:
        # Connect to the MySQL server (no database selected yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sojifunmi1#"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database only if it does not exist (no SELECT/SHOW used)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection cleanly
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()