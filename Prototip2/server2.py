from dadesPro2 import users  # Importamos la lista de usuarios
from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos
users = [
    {"id": 1, "username": "mare", "email": "mare@gmail.com"},
    {"id": 2, "username": "pare", "email": "pare@gmail.com"}
]

children = [
    {"id": 1, "name": "Laura Child", "sleep_average": 8, "treatment": "Hour", "time": 6},
    {"id": 2, "name": "Christian Child", "sleep_average": 6, "treatment": "percentage", "time": 4}
]


# Ruta para obtener un usuario por nombre de usuario
@app.route('/prototip2/getuser', methods=['GET'])
def get_user():
    username = request.args.get('username')
    user = next((u for u in users if u["username"] == username), None)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "Usuari no trobat"}), 404


# Ruta para obtener los niños asociados a un usuario (por simplicidad, asumimos todos los niños están relacionados con cualquier usuario)
@app.route('/prototip2/getchildren/<username>', methods=['GET'])
def get_children(username):
    user = next((u for u in users if u["username"] == username), None)
    if user:
        return jsonify(children), 200
    else:
        return jsonify({"error": "No children found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10050, debug=True)
