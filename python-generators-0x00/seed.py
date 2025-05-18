#!/usr/bin/python3

import psycopg2
import csv
import uuid
import os
import sys

# Database credentials
DB_HOST = 'localhost'
DB_NAME = 'alx_prodev'
DB_USER = 'postgres'
DB_PASSWORD = 'adrian'
CSV_FILE = 'user_data.csv'

# Connect to the default 'postgres' database
def connect_db():
    """
    Connect to the default 'postgres' database for administrative tasks (like creating a new database).
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname='postgres',
            user=DB_USER,
            password=DB_PASSWORD
        )
        print('Connected to PostgreSQL successfully.')
        return conn
    except Exception as e:
        print(f'Error connecting to database: {e}')
        sys.exit(1)

# Create database if not exists
def create_database(connection):
    try:
        connection.autocommit = True
        with connection.cursor() as cur:
            cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
            exists = cur.fetchone()
            if not exists:
                cur.execute(f"CREATE DATABASE {DB_NAME};")
    except Exception as e:
        print(f'Error creating database: {e}')
        sys.exit(1)

# Connect to alx_prodev database
def connect_to_prodev():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f'Error connecting to alx_prodev: {e}')
        sys.exit(1)

# Create user_data table if not exists
def create_table(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user_data (
                    user_id UUID PRIMARY KEY,
                    name VARCHAR NOT NULL,
                    email VARCHAR NOT NULL,
                    age INTEGER NOT NULL
                );
            """)
            conn.commit()
            print('Table user_data created successfully.')
    except Exception as e:
        print(f'Error creating table: {e}')
        conn.rollback()
        sys.exit(1)

# Insert data from CSV (accepts filename)
def insert_data(conn, csv_file):
    """
    Inserts user data from a CSV file into the 'user_data' table in the database.

    Args:
        conn: A database connection object supporting the context manager protocol and cursor creation.
        csv_file (str): Path to the CSV file containing user data with columns 'name', 'email', and 'age'.

    Raises:
        SystemExit: If the CSV file is not found or an error occurs during data insertion.

    The function reads each row from the CSV file, generates a unique user_id for each entry,
    and inserts the data into the 'user_data' table. If an error occurs, the transaction is rolled back
    and the program exits with an error message.
    """
    if not os.path.exists(csv_file):
        print(f'CSV file {csv_file} not found.')
        sys.exit(1)
    try:
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            with conn.cursor() as cur:
                for row in reader:
                    user_id = str(uuid.uuid4())
                    name = row['name']
                    email = row['email']
                    age = int(row['age'])
                    cur.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (user_id, name, email, age)
                    )
                conn.commit()
        print('Data inserted successfully.')
    except FileNotFoundError:
        print(f'CSV file {csv_file} not found.')
        sys.exit(1)
    except Exception as e:
        print(f'Error inserting data: {e}')
        conn.rollback()
        sys.exit(1)

def main():
    try:
        initial_conn = connect_db()
        create_database(initial_conn)
        initial_conn.close()
    except Exception as e:
        print(f'Error during initial connection: {e}')
        sys.exit(1)

    conn = connect_to_prodev()
    create_table(conn)
    insert_data(conn, CSV_FILE)
    conn.close()

if __name__ == '__main__':
    main()
