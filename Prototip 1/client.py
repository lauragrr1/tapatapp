import requests

class User:

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f"Id: {self.id}, Username: {self.username}, Password: {self.password}, Email: {self.email}"


class UserDAO:
    def getUserByUsername(username):
        response = requests.get(f'http://localhost:10050/Prototip1/getuser?username={username}')
        if response.status_code == 200:
            user_data = response.json()
            user = User(user_data['id'], user_data['username'], user_data['password'], user_data['email'])
            return user
        else:
            return None

class ViewConsole:
    def getInputUsername():
        return input("Enter username: ")

    def showUserInfo(username):
        user = UserDAO.getUserByUsername(username)
        if user:
            print(f"User Info: {user}")
        else:
            print(f"User with username {username} not found")


if __name__ == "__main__":
    username = ViewConsole.getInputUsername()
    ViewConsole.showUserInfo(username)