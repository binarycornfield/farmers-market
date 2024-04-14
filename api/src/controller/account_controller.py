import bcrypt
import os
from dotenv import load_dotenv
from model.user import User
load_dotenv()
pepper = os.getenv('PEPPER', 'test')
if pepper == 'test':
    print('Pepper not set')
def hash_password(password):
    # Convert the password (with optional pepper) to bytes, if the pepper is used.
    password_bytes = (password + pepper).encode('utf-8')
    
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    return hashed_password

def check_password(hashed_password, provided_password):
    password_bytes = (provided_password + pepper).encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
def create_user(data):
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    hashed_password = hash_password(password)
    new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
    new_user.create()
    return new_user

