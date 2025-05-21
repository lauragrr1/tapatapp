from flask import Flask, request, jsonify, g
import dadesP3 as dades
import jwt
import datetime
from functools import wraps

# DAOs de les classes que utilitzarem
class DAOUsers:
    def __init__(self):
        self.users = dades.users

    def getUserByUsername(self, username):
        for u in self.users:
            if u.username == username:
                return u.__dict__
        return None

class DAORoles:
    def __init__(self):
        self.roles = dades.roles

    def getRolById(self, rol_id):
        for rol in self.roles:
            if rol.id == rol_id:
                return rol.type_rol
        return None

class DAOChild:
    def __init__(self):
        self.children = dades.children
        self.relations = dades.relation_user_child
        self.treatments = dades.treatments

    def getChildrenByUserId(self, user_id):
        result = []
        allowed_roles = [1, 2, 3]  # comprovació de rols

        for relation in self.relations:
            if relation["user_id"] == user_id and relation["rol_id"] in allowed_roles:
                for child in self.children:
                    if child.id == relation["child_id"]:  # Accés correcte a child_id
                        treatment = self.getTreatmentById(child.treatment_id)
                        result.append({
                            "id": child.id,
                            "name": child.child_name,
                            "sleep_average": child.sleep_average,
                            "treatment": treatment.name if treatment else "Cap tractament",
                            "time": child.time
                        })
        return result

    def getTreatmentById(self, treatment_id):
        for treatment in self.treatments:
            if treatment.id == treatment_id:
                return treatment
        return None

# Configuració Flask
app = Flask(__name__)
daoChild = DAOChild()
daoUser = DAOUsers()
app.config["SECRET_KEY"] = "1234user"  # Canvia això per una clau més segura!

# Middleware per verificar el token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token d'autenticació requerit"}), 403
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            g.user_id = data["user_id"]
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirat"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token invàlid"}), 401
        return f(*args, **kwargs)
    return decorated

# Endpoint de login
@app.route('/prototip3/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = daoUser.getUserByUsername(username)
    if user and user["password"] == password:
        token = jwt.encode(
            {"user_id": user["id"], "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1000)},
            app.config["SECRET_KEY"],
            algorithm="HS256"
        )
        return jsonify({"token": token, "username": user["username"], "email": user["email"]}), 200
    else:
        return jsonify({"error": "Usuari o contrasenya incorrectes"}), 401

# Endpoint per obtenir dades d'un usuari
@app.route('/prototip3/getuser/', methods=['GET'])
@token_required
def get_user():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "No s'ha proporcionat cap nom d'usuari"}), 400

    user = daoUser.getUserByUsername(username)
    if user:
        return jsonify({
            "id": user["id"],
            "username": user["username"],
            "email": user["email"]
        }), 200
    else:
        return jsonify({"error": "Usuari no trobat..."}), 404

# Endpoint per obtenir els infants associats a un usuari
@app.route('/prototip3/getchildren/<username>', methods=['GET'])
def get_children(username):
    user = daoUser.getUserByUsername(username)
    if not user:
        return jsonify({"error": "Usuari no trobat..."}), 404 

    children = daoChild.getChildrenByUserId(user["id"])
    if children:
        return jsonify(children), 200
    else:
        return jsonify({"error": "Aquest usuari no té nens associats"}), 404

# Iniciar el servidor Flask
if __name__ == '__main__':
    app.run(debug=True) #192.168.144.160 , host="0.0.0.0", port=10050