import psycopg2
import os
from psycopg2 import extras
def create_user():
    first_name = 'max'
    last_name = 'lemke'
    email = 'test@test.com'
    password = 'test'
    sql = """
        INSERT INTO users(first_name, last_name, email, password) 
        VALUES (%s, %s, %s, %s);"""
    user_data = (first_name, last_name, email, password)

    with conn.cursor() as cur:
        cur.execute(sql, user_data)
# Database connection parameters
host_conn = os.environ['PGHOST']
port_var = os.environ['PGPORT']
user_var = os.environ['PGUSER']
passwd = os.environ['PGPASSWORD']

# Establishing the connection
conn = psycopg2.connect(
        host=host_conn,
        port=port_var,
        user=user_var,
        password=passwd,
        dbname='farmers_market'
    )

# Creating a cursor object using the cursor() method with DictCursor
cursor = conn.cursor(cursor_factory=extras.DictCursor)
create_user()

# Executing an SQL query
cursor.execute('SELECT * FROM users')

# Fetching all rows from the database
data = cursor.fetchall()

# Converting the data into a list of dictionaries
data_as_dict = [dict(row) for row in data]

# Closing the cursor and connection
cursor.close()
conn.close()

# Output the data as a dictionary
print(data_as_dict)
