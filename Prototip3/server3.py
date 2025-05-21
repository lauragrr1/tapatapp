import hashlib
import dadesServer
from dadesServer import User, Child, Tap
from flask import Flask, jsonify, request

TOKEN_VALID = "secret123"

token = hashlib.sha256(TOKEN_VALID.encode()).hexdigest()
print(f"Generated token: {token}")

class DAOUser:
    def __init__(self):
        self.users = dadesServer.users

    def getUserById(self, user_id):
        for user in self.users:
            if user_id == user.id:
                return user
        return None

    def getUserByCredentials(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

class DAOChild:
    def __init__(self):
        self.children = dadesServer.children
        self.taps = dadesServer.taps

    def getChildByUserId(self, user_id):
        child_ids = [rel["child_id"] for rel in dadesServer.relation_user_child if rel["user_id"] == int(user_id)]
        children = [child for child in self.children if child.id in child_ids]
        return children
        
    def getTapByChildId(self, child_id):
        taps = [tap for tap in self.taps if tap.child_id == int(child_id)]
        return taps

DAOUser = DAOUser()
DAOChild = DAOChild()
app = Flask(__name__)

#Metode actualitzat per a fer login amb POST y amb token
@app.route('/tapatapp/getUserByCredentials', methods=['POST'])
def getUserByCredentials():

    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header.split(" ")[1] != token:
        return jsonify({"error": "accés no autoritzat"}), 401
    
    data = request.get_json()
    id = data.get('id')
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    if username is None or password is None:
            return jsonify({"error": "falten parametres"}), 400
    
    user = DAOUser.getUserByCredentials(username, password)
    if user is None:
        return jsonify({"error": "Credencials incorrectes"}), 401
    
    return jsonify({"id": id,
                    "username": username,
                    "password": password,
                    "email": email})

@app.route('/tapatapp/getChildByUserId', methods=['GET'])
def getChildByUserId():
    user_id = request.args.get('user_id')
    children = DAOChild.getChildByUserId(user_id)
    if children:
        return jsonify([child.__dict__ for child in children])
    else:
        return jsonify({"error": "Children not found"}), 404

@app.route('/tapatapp/getTapByChildId', methods=['GET'])
def getTapByChildId():
    child_id = request.args.get('child_id')
    taps = DAOChild.getTapByChildId(child_id)
    if taps:
        return jsonify([tap.__dict__ for tap in taps])
    else:
        return jsonify({"error": "Taps not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)