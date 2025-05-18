#!/usr/bin/python3
"""
4-stream_ages.py
Calculates the average age of users using a memory-efficient generator.
"""
import psycopg2
import psycopg2.extras
seed = __import__('seed')

def stream_user_ages():
    """
    Generator function that yields user ages one by one from the database.
    Yields:
        int: Age of each user.
    """
    try:
        # Connect to the PostgreSQL database
        connection = seed.connect_to_prodev()
        cursor = connection.cursor()

        # Execute the query to fetch user ages one by one
        cursor.execute("SELECT age FROM user_data;")

        for row in cursor:
            yield row[0]  # Yield the age from the result set

        cursor.close()
        connection.close()

    except psycopg2.Error as err:
        print(f"Database error: {err}")

def calculate_average_age():
    """
    Calculates the average age of users using the age generator.
    Prints the result.
    """
    total_age = 0
    count = 0

    # Using the generator to iterate over ages
    for age in stream_user_ages():
        total_age += age
        count += 1

    # Avoid division by zero
    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")
    else:
        print("No users found.")

# Run the average calculation
if __name__ == "__main__":
    calculate_average_age()
