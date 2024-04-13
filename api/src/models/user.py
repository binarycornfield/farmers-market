import psycopg2
from psycopg2.extras import DictCursor

conn = psycopg2.connect()

class User:
    # def __init__(self, first_name, last_name, email, password):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.password = password

    def find_one(self, user_id):
        sql = f"SELECT * FROM users WHERE user_id = {user_id}"
        pass

    def find_all(self):
        sql = "SELECT * FROM users;"
        return run_query(conn, sql)

    def create(self):
        sql = f"""
        INSERT INTO users(first_name, last_name, email, password) 
        VALUES('{self.first_name}', '{self.last_name}', '{self.email}', '{self.password}')
        """

    def update(self):
        pass

    def delete(self):
        pass

def run_query(conn, query: str):
    """Run <query> against <conn>, and return a set of fn(row)."""
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute(query)
        # fn = lambda table: User(table[0], table[1], table[2], table[3])
        rows = cur.fetchall()
        print(rows)
        # return [row for row in rows]

user1 = User()
print(user1.find_all())