from flask import Flask, request, jsonify


class User:
    def __init__(self, id, username, password, email=""):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

    ''' def __str__(self): 
    return "Id:" + str(self.id) + " Username:" + self.username '''

listUsers= [
    User(1,"usuari1", "12345", "user@gmail.com"),
    User(2,"usuari2", "6789", "user2@gmail.com"),
    User(3,"usuari3","0101","user3@gmail.com"),
    User(4,"usuari4","2222", "user4@gmail.com")
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

@app.route('/Prototip1/getuser/<string:username>', methods=['GET'])
def getUser(username):
    if username is None or username.strip() == "":
        return jsonify({"error": "Falta el parámetro de usuario"}), 400 # Código 400: Bad Request
    
    user = daoUser.getUserByUsername(username)

    if user:
        return jsonify({
            "data": {
                "Username": user.username,
                "ID:": user.id,
                "Email": user.email
            } }), 200 # Código 200 OK
    else
        return jsonify({"error": "Usuario no encontrado"}), 400 # Código 404: No encontrado
    
@app.route('/tapatapp/getuser/<string:username>',methods=['GET'])
def get_Users ():
    n = str(request.args.get('username'))
    email = str(request.args.get('email'))
    return "Hello " + n + ", email: " + email


if __name__ == '__main__':
     app.run(debug=True,host="192.168.144.63",port="10050")