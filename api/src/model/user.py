import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Database connection established.")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")



class User:
    def __init__(self, user_id=None, first_name=None, last_name=None, email=None, password=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def find_one(self):
        sql = "SELECT * FROM users WHERE user_id = %s"
        conn = connect_db()
        return run_query(conn, sql, (self.user_id,), fetchone=True)

    def find_all(self):
        sql = "SELECT * FROM users;"
        conn = connect_db()
        return run_query(conn, sql)

    def create(self):
        sql = """
        INSERT INTO users(first_name, last_name, email, password) 
        VALUES (%s, %s, %s, %s) RETURNING user_id;
        """
        conn = connect_db()
        self.user_id = run_query(conn, sql, (self.first_name, self.last_name, self.email, self.password), commit=True)

    def update(self):
        sql = """
        UPDATE users SET first_name=%s, last_name=%s, email=%s, password=%s 
        WHERE user_id=%s;
        """
        conn = connect_db()
        run_query(conn, sql, (self.first_name, self.last_name, self.email, self.password, self.user_id), commit=True)

    def delete(self):
        sql = "DELETE FROM users WHERE user_id = %s;"
        conn = connect_db()
        run_query(conn, sql, (self.user_id,), commit=True)

def run_query(conn, query: str, params=None, commit=False, fetchone=False):
    """Run a query against <conn> with <params>, optionally committing the transaction, and fetch results based on <fetchone>."""
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute(query, params or ())
        if commit:
            conn.commit()
        conn.close()
        return cur.fetchone() if fetchone else cur.fetchall()
def database_connection()