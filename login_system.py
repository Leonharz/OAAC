import json
import hashlib
import getpass
import os
import sys

USERS_FILE = 'users.json'

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    users = load_users()
    username = input('Username: ').strip()
    if username in users:
        print('Username already exists')
        return
    password = getpass.getpass('Password: ')
    users[username] = hash_password(password)
    save_users(users)
    print('User registered successfully')


def login():
    users = load_users()
    username = input('Username: ').strip()
    password = getpass.getpass('Password: ')
    hashed = hash_password(password)
    if users.get(username) == hashed:
        print('Login successful')
    else:
        print('Invalid username or password')


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {'register', 'login'}:
        print('Usage: python3 login_system.py [register|login]')
        return
    if sys.argv[1] == 'register':
        register()
    else:
        login()


if __name__ == '__main__':
    main()
