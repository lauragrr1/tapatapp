from flask import Flask, request, jsonify
from dadesP3 import DAOUser

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    auth_header = request.headers.get('Authorization')
    if (auth_header):
        token = auth_header.split(" ")[1] if " " in auth_header else auth_header
        user = next((u for u in DAOUser.get_all_users() if u.token == token), None)
        if user:
            id_role = -1
            list_id_roles = DAOUser.get_user_role(user.id)
            if 2 in list_id_roles:
                id_role = 2
            return jsonify({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "token": token,
                "idrole": id_role,
                "msg": "Usuari Ok",
                "coderesponse": "1"
            }), 200
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

    # Existing username/password login
    data = request.get_json()
    identifier = data.get('username')  # username or email
    password = data.get('password')
    user = DAOUser.login(identifier, password)
    if user:
        id_role = -1
        list_id_roles = DAOUser.get_user_role(user.id)
        if 2 in list_id_roles:
            id_role = 2
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "token": user.token,  # Use the user's token
            "idrole": id_role,
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200
    else:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10050, debug=True)