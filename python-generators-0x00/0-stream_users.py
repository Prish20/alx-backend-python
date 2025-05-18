#!/usr/bin/python3

"""
0-stream_users.py

Defines a generator function to stream user data from PostgreSQL one row at a time.
"""

import psycopg2

def stream_users():
    """
    Connects to the PostgreSQL database and yields each row from the user_data table as a dictionary.
    Yields:
        dict: {'user_id': 'UUID', 'name': 'Name', 'email': 'Email', 'age': Age}
    Handles connection errors and ensures resources are closed properly.
    """
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            dbname='alx_prodev',
            user='postgres',
            password='adrian'
        )
        cur = conn.cursor()
        cur.execute("SELECT user_id, name, email, age FROM user_data;")
        for row in cur:
            yield {
                'user_id': str(row[0]),
                'name': row[1],
                'email': row[2],
                'age': row[3]
            }
    except Exception as e:
        print(f"Error streaming users: {e}")
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
