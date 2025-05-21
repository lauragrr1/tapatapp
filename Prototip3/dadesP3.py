class User:
    def __init__(self, id, username, password, email, token):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.token = token

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"


class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

    def __str__(self):
        return f"Child(id={self.id}, name={self.child_name})"


class Role:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

    def __str__(self):
        return f"Role(id={self.id}, type_rol={self.type_rol})"


class DAOUser:
    def __init__(self):
        self.users = [
            User(id=1, username="mare", password="12345", email="prova@gmail.com", token="token12345"),
            User(id=2, username="pare", password="123", email="prova2@gmail.com", token="token67890")
        ]

    def login(self, identifier, password):
        for user in self.users:
            if (user.username == identifier or user.email == identifier) and user.password == password:
                return user
        return None

    def get_all_users(self):
        return self.users


class DAOChild:
    def __init__(self):
        self.children = [
            Child(id=1, child_name="Carol Child", sleep_average=8, treatment_id=1, time=6),
            Child(id=2, child_name="Jaco Child", sleep_average=10, treatment_id=2, time=6)
        ]
        self.relations = [
            {"user_id": 1, "child_id": 1, "rol_id": 1},
            {"user_id": 1, "child_id": 2, "rol_id": 1},
            {"user_id": 1, "child_id": 1, "rol_id": 2},
            {"user_id": 2, "child_id": 2, "rol_id": 1},
            {"user_id": 2, "child_id": 2, "rol_id": 2}
        ]

    def get_children_by_user_id(self, user_id):
        child_ids = [relation['child_id'] for relation in self.relations if relation['user_id'] == user_id]
        return [child for child in self.children if child.id in child_ids]


class DAORole:
    def __init__(self):
        self.roles = [
            Role(id=1, type_rol="Admin"),
            Role(id=2, type_rol="Tutor Mare Pare"),
            Role(id=3, type_rol="Cuidador"),
            Role(id=4, type_rol="Seguiment")
        ]

    def get_roles(self):
        return self.roles


# Ejemplo de uso
if __name__ == "__main__":
    dao_user = DAOUser()
    dao_child = DAOChild()
    dao_role = DAORole()

    # Probar login
    user = dao_user.login("mare", "12345")
    if user:
        print(f"Inicio de sesión exitoso: {user}")
        children = dao_child.get_children_by_user_id(user.id)
        print(f"Niños asociados al usuario {user.username}:")
        for child in children:
            print(child)
    else:
        print("Credenciales incorrectas.")

    # Mostrar roles
    print("\nRoles disponibles:")
    for role in dao_role.get_roles():
        print(role)