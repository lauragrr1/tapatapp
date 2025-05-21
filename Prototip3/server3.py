from flask import Flask, request, jsonify
from dadesP3 import DAOUser  # Asegúrate de que este módulo esté correctamente implementado

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Verificar si se envió un token en el encabezado Authorization
    auth_header = request.headers.get('Authorization')
    if auth_header:
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

    # Si no hay token, intentar autenticación con username y password
    data = request.get_json()
    if not data:
        return jsonify({"msg": "No se enviaron datos"}), 400

    identifier = data.get('username')  # Puede ser username o email
    password = data.get('password')
    if not identifier or not password:
        return jsonify({"msg": "Faltan credenciales"}), 400

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
            "token": user.token,  # Usar el token del usuario
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
    # Configurar el servidor para escuchar en el puerto 10050
    app.run(host='0.0.0.0', port=10050, debug=True)