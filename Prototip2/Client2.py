# Aquest client de consola fa el següent:
# Recull el username de l'usuari.
# Obté la informació de l'usuari pel seu username.

import requests
from flask import Flask, jsonify  # Import Flask and jsonify from Flask
from dadesPro2 import User, Child, Tap, Role, Status, Treatment

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def __str__(self):
        return f"[User] ID: {self.id}, Username: {self.username}, Email: {self.email}"


class Child:
    def __init__(self, id, name, sleep_average, treatment, time):
        self.id = id
        self.name = name
        self.sleep_average = sleep_average
        self.treatment = treatment
        self.time = time

    def __str__(self):
        return f"[Child] ID: {self.id}, Name: {self.name}, Sleep Avg: {self.sleep_average}, Treatment: {self.treatment}, Time: {self.time}h"


class APIClient:
    BASE_URL = "http://127.0.0.1:10050/Prototip2"  # Assegura't que és l'adreça correcta

    @staticmethod
    def login(username, password):
        try:
            # Enviem una petició POST amb les credencials
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

    @staticmethod
    def get_user(username):
        try:
            response = requests.get(f"{APIClient.BASE_URL}/getuser", params={"username": username})
            print(f"Resposta de l'API: {response.status_code}, {response.text}")  # Depuració
            if response.status_code == 200:
                data = response.json()
                return User(data['id'], data['username'], data['email'])
            else:
                print(f"Error: {response.json().get('error', 'Usuari no trobat')}")
                return None
        except Exception as e:
            print(f"Connection Error: {e}")
            return None

    @staticmethod
    def get_children(username):
        try:
            response = requests.get(f"{APIClient.BASE_URL}/getchildren/{username}")
            # if response.status_code == 200:
            #     children = response.json()
            #     return [Child(c["id"], c["name"], c["sleep_average"], c["treatment_id"], c["time"]) for c in children]
            if response.status_code == 200:
                children_data = response.json()
                return [Child(c["id"], c["name"], c["sleep_average"], c["treatment"], c["time"]) for c in children_data]
                #children = [Child(c["id"], c["name"], c["sleep_average"], c["treatment"], c["time"]) for c in children_data]
            else:
                print(f"Error: {response.json().get('error', 'No children found')}")
                return []
        except Exception as e:
            print(f"Connection Error: {e}")
            return []

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

            if option == "1":  # Login
                username = input("Introdueix el nom d'usuari: ")
                password = input("Introdueix la contrasenya: ")
                user = APIClient.login(username, password)
                if user:
                    print(f"Benvingut/da, {user['user']['username']}!")
                else:
                    print("Login fallit. Credencials incorrectes.")

            elif option == "2":  # Consultar Usuari
                username = input("Introdueix el nom d'usuari: ")
                user = APIClient.get_user(username)
                if user:
                    print(user)
                else:
                    print("Usuari no trobat.")

            elif option == "3":  # Consultar Nens de l'Usuari
                username = input("Introdueix el nom d'usuari: ")
                children = APIClient.get_children(username)
                if children:
                    for child in children:
                        print(child)
                else:
                    print("Aquest usuari no té nens associats.")

            elif option == "4":  # Sortir
                print("Sortint...")
                break

            else:
                print("Opció incorrecta. Torna a intentar-ho.")

if __name__ == "__main__":
    ConsoleView.run()

app = Flask(__name__)  # Initialize the Flask app
print("Servidor iniciat correctament")

@app.route('/Prototip2/getchildren/<username>', methods=['GET'])
def get_children(username):
    from dadesPro2 import UserDAO, ChildDAO  
    user_dao = UserDAO()
    user = user_dao.getUserByCredentials(username)

    if not user:
        return jsonify({"error": "Usuari no trobat"}), 404

    child_dao = ChildDAO()
    children = child_dao.getChildByUser(user['id'])

    if children:
        return jsonify(children), 200
    else:
        return jsonify({"error": "No hi ha nens associats a aquest usuari"}), 404