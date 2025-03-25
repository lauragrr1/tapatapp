import requests

# Clase Usuario
class Usuario:
    def __init__(self, id, nombre, email, contraseña):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
    
    def login(self):
        print(f"{self.nombre} ha iniciado sesión con éxito.")
    
    def registrar(self):
        print(f"{self.nombre} ha sido registrado con éxito.")
    
    def recuperarContraseña(self):
        print(f"Contraseña de {self.nombre} recuperada con éxito.")
    
    def cerrarSesion(self):
        print(f"{self.nombre} ha cerrado sesión.")

# Clase Niño
class Nino:
    def __init__(self, nombre, edad, horasActivas):
        self.nombre = nombre
        self.edad = edad
        self.horasActivas = horasActivas
    
    def seleccionarNiño(self):
        print(f"Niño seleccionado: {self.nombre}, Edad: {self.edad}")
    
    def verHorasActivas(self):
        print(f"{self.nombre} tiene {self.horasActivas} horas activas.")

# Clase Configuración
class Configuración:
    def __init__(self, configuracionesGenerales):
        self.configuracionesGenerales = configuracionesGenerales
    
    def editarPerfil(self):
        print("Perfil editado con éxito.")
    
    def modificarDatosPersonales(self):
        print("Datos personales modificados con éxito.")

# Clase RecuperaciónContraseña
class RecuperacionContraseña:
    def __init__(self, email, nuevaContraseña):
        self.email = email
        self.nuevaContraseña = nuevaContraseña
    
    def recuperarContraseña(self):
        print(f"Contraseña para {self.email} recuperada con éxito.")

# Clase Contacto
class Contacto:
    def __init__(self, nombre, email, mensaje):
        self.nombre = nombre
        self.email = email
        self.mensaje = mensaje
    
    def enviarMensaje(self):
        print(f"Mensaje enviado de {self.nombre} a {self.email}: {self.mensaje}")

# Clase PantallaPrincipal
class PantallaPrincipal:
    def __init__(self):
        self.listaDeNinos = []
    
    def seleccionarNiño(self, nino):
        self.listaDeNinos.append(nino)
        print(f"Niño {nino.nombre} añadido a la lista.")
    
    def verHorasActivas(self, nino):
        nino.verHorasActivas()
    
    def configurar(self, configuracion):
        print("Configuración abierta.")
        configuracion.editarPerfil()
        configuracion.modificarDatosPersonales()
    
    def cerrarSesion(self, usuario):
        usuario.cerrarSesion()

# Simulación de interacción con el usuario (cliente)
class Cliente:
    def __init__(self):
        # Creación de objetos
        self.usuario = Usuario(1, "Juan", "juan@example.com", "password123")
        self.pantallaPrincipal = PantallaPrincipal()
        self.configuracion = Configuración("Configuración General")
        self.nino = Nino("Carlos", 8, 50)
    
    def login(self):
        self.usuario.login()
        self.pantallaPrincipal.seleccionarNiño(self.nino)
    
    def mostrarInformacionNiño(self):
        self.pantallaPrincipal.verHorasActivas(self.nino)
    
    def editarConfiguracion(self):
        self.pantallaPrincipal.configurar(self.configuracion)
    
    def cerrarSesion(self):
        self.pantallaPrincipal.cerrarSesion(self.usuario)

# Interacción del cliente
if __name__ == "__main__":
    cliente = Cliente()
    cliente.login()  # Iniciar sesión
    cliente.mostrarInformacionNiño()  # Ver horas activas de un niño