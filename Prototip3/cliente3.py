import requests
import tkinter as tk
from tkinter import messagebox

class DAOUser:
    @staticmethod
    def getUserByCredentials(username, password):
        response = requests.post("http://localhost:10050", json={"username": username, "password": password})

        if response.status_code == 200:
            userData = response.json()
            return userData  # Devuelve un diccionario con ID, username, email y token
        else:
            return None

class DAOChild:
    @staticmethod
    def getChildren(user_id, token):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"http://localhost:10050{user_id}", headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login App")

        # Crear los frames para las pantallas
        self.login_frame = tk.Frame(root)
        self.info_frame = tk.Frame(root)

        # Inicializar las pantallas
        self.init_login_screen()
        self.init_info_screen()

        # Mostrar la pantalla de inicio de sesión
        self.show_frame(self.login_frame)

    def init_login_screen(self):
        # Configurar la pantalla de inicio de sesión
        self.login_frame.pack(fill="both", expand=True)

        # Etiqueta y entrada para el username
        username_label = tk.Label(self.login_frame, text="Username:")
        username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(pady=10)

        # Etiqueta y entrada para el password
        password_label = tk.Label(self.login_frame, text="Password:")
        password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=10)

        # Botón para iniciar sesión
        login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        login_button.pack(pady=20)

    def init_info_screen(self):
        # Configurar la pantalla de información
        self.info_frame.pack(fill="both", expand=True)

        # Área de texto para mostrar la información del usuario y los niños
        self.info_text = tk.Text(self.info_frame, height=20, width=70, state="disabled")
        self.info_text.pack(pady=20)

        # Botón para regresar a la pantalla de inicio de sesión
        back_button = tk.Button(self.info_frame, text="Back", command=lambda: self.show_frame(self.login_frame))
        back_button.pack(pady=10)

    def show_frame(self, frame):
        # Cambiar el tamaño de la ventana según el frame
        if frame == self.login_frame:
            self.root.geometry("400x300")  # Tamaño para la pantalla de login
        elif frame == self.info_frame:
            self.root.geometry("600x450")  # Tamaño para la pantalla de información

        # Ocultar todos los frames y mostrar el seleccionado
        self.login_frame.pack_forget()
        self.info_frame.pack_forget()
        frame.pack(fill="both", expand=True)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Por favor, introduce username y password.")
            return

        user = DAOUser.getUserByCredentials(username, password)
        if user:
            self.display_user_info(user)
            self.get_children_info(user)
            self.show_frame(self.info_frame)  # Cambiar a la pantalla de información
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    def display_user_info(self, user):
        self.info_text.config(state="normal")
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, "✅ Inicio de sesión correcto!\n")
        self.info_text.insert(tk.END, " --- User Info --- \n")
        self.info_text.insert(tk.END, f"ID: {user['id']}\n")
        self.info_text.insert(tk.END, f"Username: {user['username']}\n")
        self.info_text.insert(tk.END, f"Email: {user['email']}\n")
        self.info_text.insert(tk.END, f"Token: {user['token']}\n")
        self.info_text.config(state="disabled")

    def get_children_info(self, user):
        user_id = user['id']
        token = user['token']
        children = DAOChild.getChildren(user_id, token)

        self.info_text.config(state="normal")
        if children:
            self.info_text.insert(tk.END, "\n👶 --- Children Info --- \n")
            for child in children:
                self.info_text.insert(tk.END, f"ID: {child['id']}\n")
                self.info_text.insert(tk.END, f"Nombre: {child['child_name']}\n")
                self.info_text.insert(tk.END, f"Promedio de sueño: {child['sleep_average']} horas\n\n")
        else:
            self.info_text.insert(tk.END, "\n❌ ERROR: No hay niños asociados a este usuario.\n")
        self.info_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()