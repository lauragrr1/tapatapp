import dadesPro2 as server
from dadesPro2 import User, Child, Tap, Role, Status, Treatment
from flask import Flask, request, jsonify

app = Flask(__name__)

############  DAOs  ############

class UserDAO:
    def __init__(self):
        self.users = server.users

    def get_all_users(self):
        return [user.__dict__ for user in self.users]

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None

class ChildDAO:
    def __init__(self):
        self.children = server.children

    def get_all_children(self):
        # Inicialitzar una llista buida per emmagatzemar els diccionaris dels fills
        children_dicts = []
        # Recórrer cada objecte 'child' en la llista 'self.children'
        for child in self.children:
            # Convertir l'objecte 'child' en diccionari i afegir-lo a la llista
            children_dicts.append(child.__dict__)
        return children_dicts

    def get_children_by_user_id(self, user_id):
        # Inicialitzar una llista buida per emmagatzemar els child_ids
        child_ids = []
        # Recórrer cada relació a la llista relation_user_child
        for rel in server.relation_user_child:
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