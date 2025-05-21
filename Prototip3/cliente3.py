import requests

class Cliente:
    BASE_URL = "http://localhost:10050"  # Cambia el puerto si es necesario

    @staticmethod
    def login(username, password):
        url = f"{Cliente.BASE_URL}/prototip2/login"
        headers = {"Content-Type": "application/json"}
        payload = {"username": username, "password": password}

        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print("✅ Inicio de sesión exitoso!")
                return response.json()  # Devuelve los datos del usuario
            elif response.status_code == 401:
                print("❌ Credenciales incorrectas.")
            else:
                print(f"⚠️ Error inesperado: {response.status_code}")
                print(response.json())
        except requests.exceptions.RequestException as e:
            print(f"❌ Error al conectar con el servidor: {e}")
        return None

    @staticmethod
    def get_user_role(user_id, token):
        url = f"{Cliente.BASE_URL}/prototip2/children/{user_id}"
        headers = {"Authorization": f"Bearer {token}"}

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print("✅ Roles obtenidos exitosamente!")
                return response.json()  # Devuelve los roles del usuario
            elif response.status_code == 404:
                print("❌ No se encontraron roles para este usuario.")
            else:
                print(f"⚠️ Error inesperado: {response.status_code}")
                print(response.json())
        except requests.exceptions.RequestException as e:
            print(f"❌ Error al conectar con el servidor: {e}")
        return None


if __name__ == "__main__":
    # Cambia las credenciales por las que existan en tu base de datos
    username = "mare"
    password = "12345"

    # Probar inicio de sesión
    user = Cliente.login(username, password)
    if user:
        print(f"Usuario: {user['username']}, ID: {user['id']}")
        token = user.get("token")

        # Probar obtención de roles
        roles = Cliente.get_user_role(user["id"], token)
        if roles:
            print("Roles del usuario:", roles)
    print("Fin del programa")