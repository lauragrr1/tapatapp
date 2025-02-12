
## Prototip 1
![Diagrama](diagramaPrototip1.png)

## HTTP Request & Response

- [Request](../Informació/http.request.md)

- [Response](../Informació/http.response.md)


## Definició dels EndPoints del WebService
Definició dels EndPoints del Servei Web:

Què necessitem per cada End-point

- <b>Descripció</b>: Servei que consulta si existeix un User per Username.
- <b>HOST</b>: 192.168.144.63:10050
- <b>End-point (URL)</b>: http://192.168.144.63:10050/Prototip1/getuser/username
- <b>Method</b>: GET
- <b>Tipus de petició</b>: application/json
- <b>Parametres que necessita la petició</b>: Username (String).
- <b>Resposta</b>: 

Si l'usuari existeix, el servei retorna: 
         


    Code 200 Ok: {
        "satus": "success",
        "message": "User found",
        "data": {
            "Username": "usuari1",
            "ID": "1"
            "Email": "user@gmail.com"
        } 
    }

Si l'usuari no existeix, retorna:    



    Code 404: {
        "satus": "error",
        "message": "User not found"
    }

Si falta el paràmetre, retorna:

    Code 400: {
        "status": "error",
        "message": "User parameter is missing"
    }


## Diagrames 
![DAO](diagramaDAO.PNG)
------
![List](diagramaList.PNG)


## <b>Datos de entrada del usuario</b>

<b>Inicio</b>
- <b>Contactar con soporte:</b> El usuario puede enviar un mensaje al equipo de asistencia técnica detallando su consulta o problema. Se presenta un formulario donde debe ingresar su correo electrónico y escribir su mensaje.
- <b>Registro:</b> El usuario debe registrarse con un correo electrónico válido y una contraseña que contenga al menos letras y números.
- <b>Inicio de sesión:</b> El acceso a la cuenta se realiza mediante correo electrónico y contraseña.
- <b>Recuperación de contraseña:</b> Si el usuario olvida su clave, puede solicitar su recuperación ingresando su correo electrónico registrado. Se enviará un enlace para restablecer la contraseña.

<b>Pantalla principal</b>
- <b>Infantes a cargo:</b> Se muestra una lista de niños bajo el cuidado del usuario.
- <b>Información del pegat:</b> Se proporciona información sobre el uso del pegat en los niños a cargo, incluyendo horas de colocación y retiro.
- <b>Configuración:</b> Se permite al usuario realizar ajustes en su perfil y en la aplicación.
  - <b>Editar perfil:</b> Opción para modificar datos personales, agregar nueva información o actualizar secciones existentes.
  - <b>Configuraciones generales:</b> Personalización de la interfaz, incluyendo opciones como modo oscuro y tamaño de texto.
  - <b>Cerrar sesión:</b> El usuario deberá confirmar antes de cerrar sesión en la aplicación.

![NouUsers](flowchartNouUser.png)