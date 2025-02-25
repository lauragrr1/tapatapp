from flask import Flask, request, jsonify

app = Flask(__name__)

class User:
    def __init__(self, id, username, password, email=""):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

    def __str__(self): 
        print("Username:" + self.username +" Email:" + self.email)

listUsers= [
    User(id=1, username="usuari1", password="12345", email="user@gmail.com"),
    User(id=2, username="usuari2", password="6789", email="user2@gmail.com"),
    User(id=3, username="usuari3", password="0101", email="user3@hotmail.com"),
    User(id=4, username="usuari4", password="2222", email="user4@hotmail.com")
]

class DAOUsers:
    def __init__(self):
        self.users=listUsers
    
    def getUserByUsername(self,username):
        for u in self.users:
            if u.username == username:
                return u
        return None

app = Flask(__name__)
daoUser = DAOUsers()

# Endpoint para buscar usuarios por username

@app.route('/Prototip1/getuser/', defaults={'username': None}, methods=['GET'])
@app.route('/prototip1/getuser/<username>', methods=['GET'])
def getUser(username):
    if username is None or username.strip() == "":
        return jsonify({
            "status": "error",
            "message": "Falta el parámetro 'usuario'"
            }), 400 # Código 400: Bad Request
    
    user = daoUser.getUserByUsername(username)

    if user:
        return jsonify({
            "satatus": "succes",
            "message": "Usuario encontrado",
            "data": {
                "Username": user.username,
                "ID:": user.id,
                "Email": user.email
            } }), 200 # Código 200 OK
    else:
        return jsonify({
            "status": "error",
            "message": "Usuario no encontrado"
            }), 400 # Código 404: No encontrado
    
@app.route('/tapatapp/getuser/',methods=['GET'])
def get_Users ():
    n = str(request.args.get('username'))
    email = str(request.args.get('email'))
    return "Hello " + n + ", email: " + email


if __name__ == '__main__':
     app.run(debug=True,host="192.168.144.63",port="10050")