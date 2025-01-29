from flask import Flask, request, jsonify


class User:
    def __init__(self, id, username, password, email=""):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

    def __str__(self):
        return "Id:" + str(self.id) + " Username:" + self.username

listUsers= [
    User(1,"usuari1", "12345", "user@gmail.com"),
    User(2,"usuari2", "6789", "user2@gmail.com"),
    User(3,"usuari3","0101","user3@gamail.com"),
    User(4,"usuari4","2222")
]

class DAOUsers:
    def __init__(self):
        self.users=listUsers
    
    def getUserByUsername(self,username):
        for u in self.users:
            if u.username == username:
                return u
        return None

daoUser = DAOUsers()

'''
u=daoUser.getUserByUsername("usuari1")
if(u):
    print(u)
else:
    print("Usuari no trobat")
'''

app = Flask(__name__)

@app.route('/Prototip1/getuser', methods=['GET'])
def getUser():
    n = str(request.args.get('username'))
    username = 'lauragrr1'
    email = 'lala@gmail.com'
    id = '235689'
    return "Hello " + n + ", email: " + email + ", ID: " + id + " Username: " + username



@app.route('/prototip/getuser/<string:username>',methods=['GET'])
def prototipGetUser(username):
    return "Prototip 1, user: " + username
s

if __name__ == '__main__':
     app.run(debug=True,host="0.0.0.0",port="10050")