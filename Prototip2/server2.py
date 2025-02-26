from flask import Flask, request, jsonify
from dadesPro2 import users, children

app = Flask(__name__)

dao_users = users()
dao_childs = children()

# Ruta per iniciar sesión¡ i obtenir informació del nen associat
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Autenticació d'usuari
    user = next((u for u in dao_users.users if u.username == username and u.password == password), None)
    if not user:
        return jsonify({"error": "Incorrect credentials"}), 401
    
    # Obtenir informació del nen associat
    children = dao_childs.getChildbyUserID(user.id)
    if not children:
        return jsonify({"message": "There are no children associated with this user"})
    
    return jsonify({"user": user.__dict__, "children": [child.__dict__ for child in children]})

if __name__ == '__main__':
    app.run(debug=True)