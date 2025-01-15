from flask import Flask, request, jsonify

# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return "Id: " + str(self.id) + "Username: " + self.username
    
listUsers= [
    User(1, "usuari1", "12345", "prova@gmail.com"),
    User(2, "usuari2", "6789", "user@gmail.com"),
    User(3, "usuari3", "0987", "admin@gmail.com"),
]

for u in listUsers:
    print(u)


# Class Dao Users
class DaoUsers:
    def __init__(self):
        self.users=listUsers

    def getUserByUsername(self,username):
        # Busca en la lista de usuarios
        for u in self.users:
            if u.username == username:
                return u
        return None  # Si no se encuentra, devuelve None

dao = DaoUsers()

u=dao.getUserByUsername("usuari1")
if(u):
    print(u)
else:
    print("No trobat")

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)