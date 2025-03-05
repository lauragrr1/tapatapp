from flask import Flask, request, jsonify

app = Flask(__name__)

class User:
    def __init__(self, id, username, password, email):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

    def __str__(self): 
        print("Username:" + self.username + " Email:" + self.email)

listUsers= [
    User(id=1, username="usuari1", password="12345", email="user@gmail.com"),
    User(id=2, username="usuari2", password="6789", email="user2@gmail.com"),
    User(id=3, username="usuari3", password="0101", email="user3@hotmail.com"),
    User(id=4, username="usuari4", password="2222", email="user4@hotmail.com")
]

class DAOUsers:
    def __init__(self):
        self.users=listUsers
    
    def get_all_users(self):
        result = []
        for user in self.users:
            result.append(user.__dict__)
        return result
    
    def getUserByUsername(self,username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None

daoUser = DAOUsers()

# Endpoint para buscar usuarios por username

@app.route('/Prototip1/listUsers', methods=['GET'])
def get_users():
    return jsonify(daoUser.get_all_users())


@app.route('/Prototip1/getuser', methods=['GET'])
def getUserByUsername():
    username=request.args.get('username', default="", type=str)
    print("+"+username+"+")
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
    

if __name__ == '__main__':
     app.run(debug=True,host="192.168.144.63",port="10050")