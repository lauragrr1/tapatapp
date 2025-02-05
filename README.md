# Projecte Tapatapp 
- [Descripció del Projecte](Informació/descripcio.md)

- [Requeriments tècnics](Informació/Requeriments.md)

## Prototip 1
![Diagrama](<Prototip 1/diagramaPrototip1.png>)

## HTTP Request & Response

- [Request](Informació/http.request.md)

- [Response](Informació/http.response.md)


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

Si falta un paràmetre, retorna:

    Code 400: {
        "status": "error",
        "message": "User parameter is missing"
    }


