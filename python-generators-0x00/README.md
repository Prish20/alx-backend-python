# Python Generators Project

## Project Overview

This project demonstrates the use of Python generators for efficient data handling, focusing on streaming data from SQL databases, batch processing, lazy loading, and memory-efficient aggregation. The project is part of the ALX program and uses PostgreSQL as the database system.

## Task 0: Getting Started with Python Generators

### Objective

Create a generator that streams rows from an SQL database one by one.

### Steps

1. **Database Setup:**

   * Created a PostgreSQL database named `alx_prodev`.
   * Created a table named `user_data` with the following fields:

     * `user_id` (Primary Key, UUID, Indexed)
     * `name` (VARCHAR, NOT NULL)
     * `email` (VARCHAR, NOT NULL)
     * `age` (INTEGER, NOT NULL)

2. **Data Insertion:**

   * Wrote a Python script (`seed.py`) to connect to the database and insert data from `user_data.csv`.
   * Successfully inserted sample data into the `user_data` table.

3. **Testing the Seed Script:**

   * Wrote a test script (`0-main.py`) to verify the data insertion.
   * Successfully fetched and displayed the first 5 rows from the `user_data` table.

### Task 1: Streaming Rows from SQL Database

### Objective(Task1)

Create a generator that streams rows from the SQL database (`user_data` table) one by one using the `yield` keyword.

### Steps(Task1)

1. **Generator Function:**

   * Implemented a generator function `stream_users()` in `0-stream_users.py`.
   * Connects to the PostgreSQL database and streams each row one by one.
   * Uses `yield` to output each row as a dictionary in the format:

     ```bash
     {'user_id': 'UUID', 'name': 'Name', 'email': 'Email', 'age': Age}
     ```

2. **Test Script:**

   * Wrote `1-main.py` to print the first 6 rows using `itertools.islice`.
   * Successfully displayed the rows in the specified format.
