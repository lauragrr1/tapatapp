# TAPATAPP

## WireFrames

![Wireframes](WireframeP2.png)

## Descripció dels view

### Pantalla d’Inici i Autenticació
- <b>Benvinguda:</b> Es mostra una pantalla amb opcions per iniciar sessió o registrar-se.
- <b>Registre d’Usuari</b>:
  	- Correu electrònic (validació requerida)
  	- Contrasenya (ha de contenir lletres i números)
- <b>Inici de Sessió</b>:
	- Accés amb correu electrònic i contrasenya.
- <b>Recuperació de Contrasenya</b>: Si l’usuari oblida la seva clau:
    1. Introdueix el correu electrònic registrat.
  	2. Rep un enllaç per restablir la contrasenya.

### Pantalla Principal
- <b>Infants a Càrrec</b>: Si l'usuari té més d’un infant a càrrec, es mostrarà una llista amb els seus noms. En seleccionar un infant, es redirigeix al < Menú de l’Infant >.

### Menú de l'Infant
- <b>Detalls de l'Infant</b>: Esmostres les dades principals:
    - Nom
    - Edat
    - Informació rellevant (Estat del pegat)
- <b>Estat del pegat</b>: Es mostra informació com:
    - Temps de col·locació
    - Temps de retirada
    - Estat actual
- <b>Configuració de l'Infant</b>: Opcions per modificar les preferències i informació associada.


## Descripció d'Implementació del Prototip 2

En aquest Prototip 2, s'implementarà un sistema de login que permetrà registrar-se i iniciar sessió amb un nom d'usuari (correu electrònic) i contrasenya. Després, a partir de les dades de l'usuari (tutor), es podrà visualitzar la informació del nen amb els taps.


## Diagrama d'arquitectura 

![ArquitecturaP2](arq2.png)

## Diagrama de classes de Backend i Front-End

### Back End

![BackEnd](BackEndP2.png)

### Front-End

![FrontEnd](FrontEndP2.png)

## Implementació

### Vista Login i Vista Child Taps

- Vista Login:

Descripció: Pantalla de Login on l'usuari es validarà.

Informació d'Entrada: Username o email, Password.

Informació que necessita la Vista: None.

Implementació:

Crear un formulari amb camps per a username/email i password.

Validar les credencials amb el backend.

Redirigir a la Vista Principal si el login és correcte.

- Vista Child Taps:

Descripció: Vista del Child que té assignat l'Usuari amb els registres d'estat del pegat.

Informació d'Entrada: None.

Informació que necessita la Vista: User, Child i Taps.

Implementació:

Mostrar una llista de taps associats al child.

Permetre a l'usuari veure els detalls de cada tap
