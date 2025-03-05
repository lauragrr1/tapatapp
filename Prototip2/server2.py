import dadesPro2 as server
from dadesPro2 import User, Child, Tap, Role, Status, Treatment
from flask import Flask, request, jsonify

app = Flask(__name__)

dao_users = users()
dao_childs = children()

# Ruta per iniciar sesión i obtenir informació del nen associat
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    
    # Verificar que los datos necesarios estén presentes en la solicitud
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400
    
    username = data['username']
    password = data['password']
    
    # Autenticació d'usuari
    user = next((u for u in dao_users.users if u.username == username and u.password == password), None)
    if not user:
        return jsonify({"error": "Incorrect credentials"}), 401
    
    # Obtenir informació del nen associat
    children = dao_childs.getChildbyUserID(user.id)
    if not children:
        return jsonify({"message": "There are no children associated with this user"})
    
    # Respuesta con los datos del usuario y los niños asociados
    return jsonify({
        "user": user.__dict__,
        "children": [child.__dict__ for child in children]
    })

if __name__ == '__main__':
    app.run(debug=True)
