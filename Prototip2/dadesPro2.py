# Dades d'exemple amb List
# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email

users = [
    User(id=1, username="mare", password="12345", email="prova@gmail.com"),
    User(id=2, username="pare", password="123", email="prova2@gmail.com")
]

# Crear les classes Child, Tap, Role, Status i Treatment

class Children:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

    def __str__(self):
        return f"{self.child_name}: {self.sleep_average} hours, Treatment ID: {self.treatment_id}, Time: {self.time} hours"

children = [
    Children(id=1, child_name="Carol Child", sleep_average=8, treatment_id=1, time=6),
    Children(id=2, child_name="Jaco Child", sleep_average=10, treatment_id=2, time=6)
]

class Taps:
    def __init__(self, id, child_id, status_id, user_id, init, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end

    def __str__(self):
        return f"Tap {self.id}: Child {self.child_id}, Status {self.status_id}, User {self.user_id}, Start: {self.init}, End: {self.end}"

taps = [
    Taps(id=1, child_id=1, status_id=1, user_id=1, init="2024-12-18T19:42:43", end="2024-12-18T20:42:43"),
    Taps(id=2, child_id=2, status_id=2, user_id=2, init="2024-12-18T21:42:43", end="2024-12-18T22:42:43")
]

relation_user_child = [
    {"user_id": 1, "child_id": 1, "rol_id": 1},
    {"user_id": 1, "child_id": 1, "rol_id": 2},
    {"user_id": 2, "child_id": 2, "rol_id": 1},
    {"user_id": 2, "child_id": 2, "rol_id": 2}
]

class Roles:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

    def __str__(self):
        return f"Role {self.id}: {self.type_rol}"

roles = [
    Roles(id=1, type_rol='Admin'),
    Roles(id=2, type_rol='Tutor Mare Pare'),
    Roles(id=3, type_rol='Cuidador'),
    Roles(id=4, type_rol='Seguiment')
]

class Statuses:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Status {self.id}: {self.name}"

statuses = [
    Statuses(id=1, name="sleep"),
    Statuses(id=2, name="awake"),
    Statuses(id=3, name="yes_eyepatch"),
    Statuses(id=4, name="no_eyepatch")
]

class Treatments:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Treatment {self.id}: {self.name}"

treatments = [
    Treatments(id=1, name='Hour'),
    Treatments(id=2, name='percentage')
]

# Prueba de impresión
for user in users:
    print(user)

for child in children:
    print(child)

for tap in taps:
    print(tap)

for role in roles:
    print(role)

for status in statuses:
    print(status)

for treatment in treatments:
    print(treatment)