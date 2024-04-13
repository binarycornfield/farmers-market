from flask import Flask, request, jsonify
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

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    sql = """
        INSERT INTO users(first_name, last_name, email, password) 
        VALUES (%s, %s, %s, %s);"""
    user_data = (first_name, last_name, email, password)

    with conn.cursor() as cur:
        cur.execute(sql, user_data)
    return jsonify({'message': 'User created successfully', 'user': email}), 201

@app.route("/users/<id>", methods=['PUT'])
def update_user(id):
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    sql = """
        UPDATE users(first_name, last_name, email, password) 
        SET first_name=%s, last_name=%s, email=%s, password=%s
        WHERE user_id=%s;
    """
    user_data = (first_name, last_name, email, password, id)

    with conn.cursor() as cur:
        cur.execute(sql, user_data)
    return jsonify({'message': 'Updated user successfully', 'user': email}), 201


@app.route("/users")
def delete_user(id):
    pass