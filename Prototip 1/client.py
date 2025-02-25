import requests

class User:

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

def __str__(self):
    return f"User(id={self.id}, username='{self.username}', email='{self.email}')"


class UserDAO:
    def __init__(self):
# Base de datos simulada
        self.users = {
        "user1": User(1, "user1", "pass1", "user1@example.com"),
        "user2": User(2, "user2", "pass2", "user2@example.com")
        }

def get_user_by_username(self, username: str):
    return self.users.get(username, None)


class ViewConsole:
    def getInputUsername(self):
        return input("Ingrese el nombre de usuario: ")

def showUserInfo(self, username: str):
    user_dao = UserDAO()
    user = user_dao.get_user_by_username(username)
    if user:
        print(f"User Info: {user}")
    else:
        print(f"User with username {username} not found")


if __name__ == "__main__":
    view = ViewConsole()
    username = ViewConsole.getInputUsername()
    ViewConsole.showUserInfo(username)