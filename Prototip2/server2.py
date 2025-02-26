import dadesPro2 as dades
from dadesPro2 import User,Child,Tap,Status,Role,Treatment
from flask import Flask, jsonify, request

# DAOs  

class UserDAO:
    def __init__(self):
        self.users = dades.users

    def get_all_users(self):
        return [user.__dict__ for user in self.users]

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None

class ChildDAO:
    def __init__(self):
        self.children = dades.children

    def get_all_children(self):
        children_dicts = []
        # Recórrer cada objecte 'child' en la llista 'self.children'
        for child in self.children:
            children_dicts.append(child.__dict__)
        return children_dicts

    def get_children_by_user_id(self, user_id):
        child_ids = []
        # Recórrer cada relació a la llista relation_user_child
        for rel in dades.relation_user_child:
            # Comprovar si el user_id de la relació coincideix amb el user_id donat
            if rel["user_id"] == user_id:
                child_ids.append(rel["child_id"])
        children_dicts = []
        for child in self.children:
            # Comprovar si l'ID del child està dins de la llista child_ids
            if child.id in child_ids:
                children_dicts.append(child.__dict__)
        return children_dicts