# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email

# Clase Child
class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

# Clase Tap
class Tap:
    def __init__(self, id, child_id, status_id, user_id, init, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end

# Clase Status
class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Clase Role
class Role:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

# Clase Treatment
class Treatment:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Users
users = [
    User(id=1, username="Mare", password="DFG123", email="mare@gmail.com"),
    User(id=2, username="Pare", password="POP098", email="pare@gmail.com")
]

# Child
children = [
    Child(id=1, child_name="Rocío Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Norman Child", sleep_average=10, treatment_id=2, time=6),
    Child(id=3, child_name="Miguel Child", sleep_average=9, treatment_id=3, time=4),
    Child(id=4, child_name="Nicole Child", sleep_average=10, treatment_id=4, time=4)
]

# Taps
taps = [
    Tap(id=1, child_id=1, status_id=1, user_id=1, init="2025-01-06T19:42:00", end="2025-01-06T22:42:00"),
    Tap(id=2, child_id=2, status_id=2, user_id=2, init="2025-01-11T21:31:00", end="2025-01-11T23:31:00"),
    Tap(id=3, child_id=3, status_id=3, user_id=1, init="2025-01-10T22:30:00", end="2025-01-11T07:30:00"),
    Tap(id=4, child_id=4, status_id=4, user_id=2, init="2025-01-15T20:55:00", end="2025-01-16T09:55:00")
]


relation_user_child = [
    {"user_id": 1, "child_id": 1, "rol_id": 2},
    {"user_id": 1, "child_id": 2, "rol_id": 2},
    {"user_id": 2, "child_id": 1, "rol_id": 2},
    {"user_id": 2, "child_id": 2, "rol_id": 2}
]

# Roles
roles = [
    Role(id=1, type_rol='Admin'),
    Role(id=2, type_rol='Tutor/Mare/Pare'),
    Role(id=3, type_rol='Cuidador'),
    Role(id=4, type_rol='Seguiment')
]

# Status
statuses = [
    Status(id=1, name="sleep"),
    Status(id=2, name="awake"),
    Status(id=3, name="yes_eyepatch"),
    Status(id=4, name="no_eyepatch")
]

#Status
treatments = [
    Treatment(id=1, name='Hour'),
    Treatment(id=2, name='percentage')
]