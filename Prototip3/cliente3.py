from dadesP3 import DAOUser

user = DAOUser.login("mare", "12345")
if user:
    print(user.username, user.id)
    id_role = DAOUser.get_user_role(user.id)
    print(id_role)
print("Fin del programa")