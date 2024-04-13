from flask import Flask, request
import psycopg2
import json
from dataclasses import dataclass
from uuid import UUID

app = Flask(__name__)

conn = psycopg2.connect()
def run_query(query, fn):
    with conn.cursor() as cur:
        cur.execute(query)
        return [fn(row) for row in cur]

@dataclass
class User:
    user_id: UUID 
    first_name: str
    last_name: str
    email: str
    password: str

@app.route("/users", methods=['GET'])
def get_users():
    sql = "SELECT * FROM users;"
    fn = lambda table: User(table[0], table[1], table[2], table[3], table[4])
    users = run_query(sql, fn)
    return users 

@app.route("/users/<id>", methods=['GET'])
def get_user(id):
    sql = f"SELECT * FROM users WHERE user_id = '{id}';"
    fn = lambda table: User(table[0], table[1], table[2], table[3], table[4])
    users = run_query(sql, fn)
    return users  

@app.route("/users", methods=['POST'])
def create_user():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        first_name = json.get("first_name")
        last_name = json.get("last_name")
        email = json.get("email")
        password = json.get("password")
        sql = f"""
            INSERT INTO users(first_name, last_name, email, password) 
            VALUES ('{first_name}', '{last_name}', '{email}', '{password}');
        """
        with conn.cursor() as cur:
            result = cur.execute(sql)
        return result

@app.route("/users")
def update_user(id):
    pass

@app.route("/users")
def delete_user(id):
    pass