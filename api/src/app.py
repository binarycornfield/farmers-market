from flask import Flask
import json

app = Flask(__name__)

users = [
    {
        "userId": "1",
        "firstName": "curtis",
        "lastName": "rubeck"
    },
    {
        "userId": "2",
        "firstName": "max",
        "lastName": "lemke"
    }
]

@app.route("/users")
def get_users():
    return json.dumps(users) 

@app.route("/users/<id>")
def get_user(id):
    for user in users:
        if user.get("userId") == id:
            return json.dumps(f"Hello user_id {user}")

def update_user(id):
    pass

def create_user():
    pass

def delete_user(id):
    pass