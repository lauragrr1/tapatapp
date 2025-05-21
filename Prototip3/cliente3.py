# Aquest client de consola recull dades d'entrada de l'usuari i les envia al servidor
# per a que les processi pel seu username. El servidor respon amb un missatge que el client mostra a la consola.

import requests

# classe usuari amb els seus atributs 
class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, Username: {self.username}, Email: {self.email}"

# la classe Child amb els seus atributs
class Child:
    def __init__(self, id, name, sleep_average, treatment, time):
        self.id = id
        self.name = name
        self.sleep_average = sleep_average
        self.treatment = treatment  
        self.time = time

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Sleep Average: {self.sleep_average}, Treatment: {self.treatment}, Time: {self.time}"
    
# classe APIClient 
class APIClient:
    BASE_URL = "http://localhost:5000/prototip3"  # port per defecte 
    token = None  # per guardar el token d'autenticació

    @staticmethod
    def login(username, password):
        try:
            response = requests.post(
                f"{APIClient.BASE_URL}/login",
                json={"username": username, "password": password},
                timeout=5  # Afegim timeout per evitar esperes infinites
            )
            
            response.raise_for_status()  # Això llançarà una excepció per codis 4XX/5XX
            
            data = response.json()
            APIClient.token = data.get("token")  # Utilitzem .get() per evitar KeyError
            if not APIClient.token:
                print("Error: El servidor no ha retornat cap token")
                return None
                
            print("Login exitós!")
            return User(
                data.get('id'),
                data.get('username'),
                data.get('email')
            )
            
        except requests.exceptions.RequestException as ex:
            print(f"Error de connexió: {ex}")
            return None
        except ValueError as ex:
            print(f"Error en el format de la resposta: {ex}")
            return None
    
    @staticmethod
    def get_user(username):
        if not APIClient.token:
            print("Error: No hi ha cap usuari autenticat.")
            return None
            
        headers = {"Authorization": f"Bearer {APIClient.token}"}  # Format estàndard per a tokens

        try:    
            response = requests.get(
                f"{APIClient.BASE_URL}/getuser",
                headers=headers,
                timeout=5
            )
            response.raise_for_status()
            
            data = response.json()
            return User(
                data.get('id'),
                data.get('username'),
                data.get('email')
            )
            
        except requests.exceptions.RequestException as ex:
            print(f"Error de connexió: {ex}")
            return None
        except ValueError as ex:
            print(f"Error en el format de la resposta: {ex}")
            return None

    @staticmethod
    def get_children(username):
        try:    
            response = requests.get(
                f"{APIClient.BASE_URL}/getchildren/{username}",
                timeout=5
            )
            response.raise_for_status()
            
            children_data = response.json()
            if not isinstance(children_data, list):
                print("Error: Format de resposta inesperat")
                return []
                
            return [
                Child(
                    child.get('id'),
                    child.get('name'),
                    child.get('sleep_average'),
                    child.get('treatment'),
                    child.get('time')
                ) 
                for child in children_data
            ]
            
        except requests.exceptions.RequestException as ex:
            print(f"Error de connexió: {ex}")
            return []
        except ValueError as ex:
            print(f"Error en el format de la resposta: {ex}")
            return []

# creem la classe ConsoleView per a gestionar la interacció amb l'usuari
class ConsoleView:
    logged_user = None

    @staticmethod
    def login():
        username = input("Introdueix el teu nom d'usuari: ")
        password = input("Introdueix la teva contrasenya: ")  
        ConsoleView.logged_user = APIClient.login(username, password)
        if not ConsoleView.logged_user:
            print("No s'ha pogut iniciar sessió. Torna-ho a provar.")

    @staticmethod
    def show_menu():
        print("\n--- MENÚ ---")
        print("1. Veure les meves dades")
        print("2. Consultar informació dels nens")
        print("3. Sortir")

    @staticmethod
    def run():
        print("Benvingut/da a l'aplicació TapatApp!")
        
        while True:
            ConsoleView.login()
            if ConsoleView.logged_user:
                break
                
        while True:
            ConsoleView.show_menu()
            option = input("Introdueix una opció (1-3): ").strip()
            
            if option == "1":
                print("\nLes teves dades:")
                print(ConsoleView.logged_user)
                
            elif option == "2":
                print("\nInformació dels nens:")
                children = APIClient.get_children(ConsoleView.logged_user.username)
                if children:
                    for child in children:
                        print(child)
                else:
                    print("No s'han trobat nens o hi ha hagut un error.")
                    
            elif option == "3":
                print("\nFins aviat! Adeu!")
                break
                
            else:
                print("Opció no vàlida. Si us plau, tria una opció entre 1 i 3.")

if __name__ == "__main__":
    ConsoleView.run()