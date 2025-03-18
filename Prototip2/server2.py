import dadesPro2 as dades
from dadesPro2 import User, Child, Tap, Role, Status, Treatment
from flask import Flask, request, jsonify

app = Flask(__name__)

############  DAOs  ############

class UserDAO:
    def __init__(self):
        self.users = dades.users

    def get_all_users(self):
        return [user.__dict__ for user in self.users]

    def getUserByCredentials(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None

class ChildDAO:
    def __init__(self):
        self.children = dades.children

    def get_all_children(self):
        # Inicialitzar una llista buida per emmagatzemar els diccionaris dels fills
        children_dicts = []
        # Recórrer cada objecte 'child' en la llista 'self.children'
        for child in self.children:
            # Convertir l'objecte 'child' en diccionari i afegir-lo a la llista
            children_dicts.append(child.__dict__)
        return children_dicts

    def getChildByUser(self, user_id):
        # Inicialitzar una llista buida per emmagatzemar els child_ids
        child_ids = []
        # Recórrer cada relació a la llista relation_user_child
        for rel in dades.relation_user_child:
            # Comprovar si el user_id de la relació coincideix amb el user_id donat
            if rel["user_id"] == user_id:
                # Afegir el child_id a la llista child_ids
                child_ids.append(rel["child_id"])
        # Inicialitzar una llista buida per emmagatzemar els diccionaris dels fills
        children_dicts = []
        # Recórrer cada objecte 'child' en la llista 'self.children'
        for child in self.children:
            # Comprovar si l'ID del child està dins de la llista child_ids
            if child.id in child_ids:
                # Afegir el diccionari de l'objecte child a la llista
                children_dicts.append(child.__dict__)
        return children_dicts
    

@app.route('/Prototip2/login', methods=['POST'])
def login():
    data = request.json  # Obtenim les dades del cos de la petició
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Falten credencials"}), 400

    user_dao = UserDAO()
    user = user_dao.getUserByCredentials(username)

    if user and user['password'] == password:  # Comprovem si la contrasenya és correcta
        return jsonify({"message": "Login correcte", "user": user}), 200
    else:
        return jsonify({"error": "Credencials incorrectes"}), 401


@app.route('/Prototip2/getuser', methods=['GET'])
def get_user():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Missing username"}), 400

    user_dao = UserDAO()
    user = user_dao.getUserByCredentials(username)

    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "Usuari no trobat"}), 404

class APIClient:
    BASE_URL = "http://127.0.0.1:10050/Prototip2"  # Assegura't que és l'adreça correcta

    @staticmethod
    def login(username, password):
        try:
            response = requests.post(f"{APIClient.BASE_URL}/login", json={"username": username, "password": password})
            if response.status_code == 200:
                print("Login correcte!")
                return response.json()  # Retornem les dades de l'usuari
            else:
                print(f"Error: {response.json().get('error', 'Credencials incorrectes')}")
                return None
        except Exception as e:
            print(f"Connection Error: {e}")
            return None

class ConsoleView:
    @staticmethod
    def menu():
        print("\n--- MENU ---")
        print("1. Login")
        print("2. Consultar Usuari")
        print("3. Consultar Nens de l'Usuari")
        print("4. Sortir")

    @staticmethod
    def run():
        while True:
            ConsoleView.menu()
            option = input("Selecciona una opció: ")

            if option == "1":
                username = input("Introdueix el nom d'usuari: ")
                password = input("Introdueix la contrasenya: ")
                user = APIClient.login(username, password)
                if user:
                    print(f"Benvingut/da, {user['user']['username']}!")
            
            elif option == "2":
                username = input("Introdueix el nom d'usuari: ")
                user = APIClient.get_user(username)
                if user:
                    print(user)
            
            elif option == "3":
                username = input("Introdueix el nom d'usuari: ")
                children = APIClient.get_children(username)
                if children:
                    for child in children:
                        print(child)
                else:
                    print("Aquest usuari no té nens associats")

            elif option == "4":
                print("Sortint...")
                break

            else:
                print("Opció incorrecta. Torna a intentar-ho.")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=10050)