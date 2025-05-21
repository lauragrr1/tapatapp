import requests
import hashlib
import dadesP3
from dadesP3 import User, Child, Tap

class DAOUser:
    pass

class DAOChild:
    @staticmethod
    def getChildByUserId(id):
        response = requests.get(f"http://127.0.0.1:5000/tapatapp/getChildByUserId?user_id={id}")
        if response.status_code == 200:
            children = []
            for data in response.json():
                children.append(Child(data['id'], data['child_name'], data['sleep_average'], data['treatment_id'], data['time']))
            return children
        else:
            print(f"Error : {response.status_code}, {response.text}")
            return None
    
    @staticmethod
    def getTapByChildId(child_id):
        response = requests.get(f"http://127.0.0.1:5000/tapatapp/getTapByChildId?child_id={child_id}")
        if response.status_code == 200:
            taps= []
            for data in response.json():
                taps.append(Tap(data['id'], data['child_id'], data['status_id'], data['user_id'], data['init'], data['end']))
            return taps
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

class View:
    @staticmethod
    def login():
        user = int(input("Enter your user id: "))
        if user < 0 or user > 1:
            print(f"Error: user with user_id:{user} doesn't exist")
            return None
        data = {
            "id": dadesP3.users[user].id,
            "username": dadesP3.users[user].username,
            "password": dadesP3.users[user].password,
            "email": dadesP3.users[user].email
        }

        TOKEN_VALID = "secret123"
        token = hashlib.sha256(TOKEN_VALID.encode()).hexdigest()

        header = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.post("http://127.0.0.1:5000/tapatapp/getUserByCredentials", json=data, headers=header)
        if response.status_code == 200:
            data = response.json()
            print("Login succesful")
            return User(data['id'], data['username'], data['password'], data['email'])
        else:
            print("Login failed")
            print(f"Error: {response.status_code}")
            return None
    
    @staticmethod
    def showUserInfo(user):
        print(user)

    @staticmethod
    def showChildInfo(child):
        print(child)

    @staticmethod
    def showTapInfo(tap):
        print(tap)


if __name__ == "__main__":
    user = View.login()
    if user:
        View.showUserInfo(user)
        children = DAOChild.getChildByUserId(user.id)
        if children:
            for child in children:
                View.showChildInfo(child)
                taps = DAOChild.getTapByChildId(child.id)
                if taps:
                    for tap in taps:
                        View.showTapInfo(tap)
                else:
                    print("No taps found for this children")
        else:
            print("No children found for this user")
