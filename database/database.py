import psycopg2
import os

# Environment variables for connection details
host_conn = os.environ['PGHOST']
port_var = os.environ['PGPORT']
user_var = os.environ['PGUSER']
farmers_market_user_pass = os.environ['FARMERSMARKETPASS']
farmers_market_user = os.environ['FARMERSMARKETUSER']
passwd = os.environ['PGPASSWORD']
def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE farmers_market")
        print("Database created successfully.")
    except psycopg2.Error as e:
        print(f"Database creation failed: {e}")

def create_table(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                user_id UUID PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                photo_url VARCHAR(2048),
                password VARCHAR(255) NOT NULL
            )
        """)
        print("Table created successfully.")
    except psycopg2.Error as e:
        print(f"Table creation failed: {e}")
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts(
                account_id UUID PRIMARY KEY,
                email VARCHAR(255) NOT NULL,
                photo_url VARCHAR(2048)
            )
        """)
        print("Table created successfully.")
    except psycopg2.Error as e:
        print(f"Table creation failed: {e}")
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users_accounts(
                account_id UUID references accounts(account_id),
                user_id UUID references users(user_id)
            )
        """)
        print("Table created successfully.")
    except psycopg2.Error as e:
        print(f"Table creation failed: {e}")

def main():
    # Connect to the default database
    conn = psycopg2.connect(
        host=host_conn,
        port=port_var,
        user=user_var,
        password=passwd,
        dbname='postgres'
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # Create the database
    create_database(cursor)

    # Close the connection to the default database
    cursor.close()
    conn.close()

    # Connect to the new database
    conn = psycopg2.connect(
        host=host_conn,
        port=port_var,
        user=user_var,
        password=passwd,
        dbname='farmers_market'
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # Create the table
    create_table(cursor)

    # Clean up: Close cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
