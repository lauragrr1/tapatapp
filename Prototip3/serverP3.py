from flask import Flask, request, jsonify
import hashlib
import random
import string


class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email

class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

class Tap:
    def __init__(self, id, child_id, status_id, user_id, init, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end

class Role:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Treatment:
    def __init__(self,  id, name):
        self.id = id
        self.name = name

users = [
    User(id=1, username="mare", password="usuari1", email="mare@gmail.com"),
    User(id=2, username="pare", password="usuari2", email="pare@gmail.com")
]

children = [
    Child(id=1, child_name="Laura Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Christian Child", sleep_average=6, treatment_id=2, time=4)
]

taps = [
    Tap(id=1, child_id=1, status_id=1, user_id=1, init="2024-12-18T19:42:43", end="2024-12-18T20:42:43"),
    Tap(id=2, child_id=2, status_id=2, user_id=2, init="2024-12-18T21:42:43", end="2024-12-18T22:42:43")
]

relation_user_child = [
    {"user_id": 1, "child_id": 1, "rol_id": 1},
    {"user_id": 1, "child_id": 1, "rol_id": 2},
    {"user_id": 2, "child_id": 2, "rol_id": 1},
    {"user_id": 2, "child_id": 2, "rol_id": 2}
]

roles = [
    Role(id=1, type_rol='Admin'),
    Role(id=2, type_rol='Tutor Mare Pare'),
    Role(id=3, type_rol='Cuidador'),
    Role(id=4, type_rol='Seguiment')
]

statuses = [
    Status(id=1, name="sleep"),
    Status(id=2, name="awake"),
    Status(id=3, name="yes_eyepatch"),
    Status(id=4, name="no_eyepatch")
]
 
treatments = [
    Treatment(id=1, name='Hour'),
    Treatment(id=2, name='percentage')
]


app = Flask(__name__)

def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=256))

@app.route('/validate_user', methods=['POST'])
def validate_user():
    data = request.json
    username_or_email = data.get('username')
    password = data.get('password')

    for user in users:
        if (user.username == username_or_email or user.email == username_or_email) and user.password == password:
            token = generate_token()
            return jsonify({"status": "success", "token": token}), 200

    return jsonify({"status": "failure", "message": "Invalid credentials"}), 401

@app.route('/validate_user2', methods=['GET'])
def validate_user_get():
    username_or_email = request.args.get('username')
    password = request.args.get('password')

    for user in users:
        if (user.username == username_or_email or user.email == username_or_email) and user.password == password:
            token = generate_token()
            return jsonify({"status": "success", "token": token}), 200

    return jsonify({"status": "failure", "message": "Invalid credentials"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10050, debug=True)