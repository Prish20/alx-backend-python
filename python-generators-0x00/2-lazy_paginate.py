#!/usr/bin/python3
"""
2-lazy_paginate.py
Implements lazy loading of paginated user data from PostgreSQL (alx_prodev.user_data).
"""
import psycopg2
import psycopg2.extras
seed = __import__('seed')

def paginate_users(page_size, offset):
    """
    Fetch a page of users from the user_data table.
    Args:
        page_size (int): Number of users per page.
        offset (int): Offset for pagination.
    Returns:
        list of dict: List of user rows as dictionaries.
    """
    try:
        # Connect to the database using seed function
        connection = seed.connect_to_prodev()
        # Use RealDictCursor to get dictionary-like row format
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(f"SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
        rows = cursor.fetchall()
        # Convert RealDictRow to a normal dictionary
        formatted_rows = [dict(row) for row in rows]
        connection.close()
        return formatted_rows
    except Exception as e:
        print(f"Database error: {e}")
        return []

def lazy_pagination(page_size):
    """
    Generator function that lazily loads each page of users.
    Args:
        page_size (int): Number of users per page.
    Yields:
        list of dict: Each page of user rows as dictionaries.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:  # No more rows to fetch
            break
        yield page  # Yield the current page as a list of dictionaries
        offset += page_size  # Move to the next page
