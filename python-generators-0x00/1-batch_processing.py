#!/usr/bin/python3

"""
1-batch_processing.py
Processes user data from the PostgreSQL database 'alx_prodev' in batches.
"""

import psycopg2
from psycopg2.extras import RealDictCursor

def stream_users_in_batches(batch_size):
    """
    Connects to the PostgreSQL database and yields batches of users from the user_data table.
    Args:
        batch_size (int): Number of users per batch.
    Yields:
        List[dict]: A batch of user records as dictionaries.
    """
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='adrian',
            database='alx_prodev'
        )
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT user_id, name, email, age FROM user_data")
            while True:
                batch = cur.fetchmany(batch_size)
                if not batch:
                    break
                yield batch
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def batch_processing(batch_size):
    """
    Processes user data in batches and prints users over age 25.
    Args:
        batch_size (int): Number of users per batch.
    """
    count = 0
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
                count += 1
                if count >= 5:
                    return
