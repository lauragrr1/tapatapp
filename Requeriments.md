# Requeriments tècnics
# 1. Backend (Servidor i Gestió de Dades)
El backend serà el cor del sistema, encarregat de gestionar dades, usuaris, i la lògica del sistema.

## a. Requisits del servidor
-Allotjament: Hosting Compartit
- Base de dades: Mysql
- Sistema operatiu del servidor: Linux
- APIs i serveis web: RESTFul Flask
## b. Llenguatges de programació
- Python

## c. Seguretat
- Autenticació i autorització
- Xifratge de dades
- Còpies de seguretat automàtiques
# 2. Frontend
## a. Tipus de Clients
- Consola Python. Escriptori.
- Llenguatge de programació: Flutter, Python Consola
- Compatibilitat dispositius: Flutter (Web, escriptori, mòbil Android,mòbil IOS)
# 3. Requisits Generals
## a. Gestió d'usuari i autenticació
- Rols d’usuari: Admin, Tutor, cuidador
- Base de dades: Mysql server
- Seguretat: Password en Md5 en BBDD
- Autenticació: login usuari o mail i contrasenya, per Token
## b. Emmagatzematge local i sincronització
- Dades que es guarden en local, són sensibles? Guardem en local Token, id usuari, nickname
- Seguretat: HTTPS, validació per token
## c. Gestió d’accessibilitat
- Nivells A, AA y AAA d’accessibilitat
# 4. Requisits d'Infraestructura
- Xarxa: Internet
- Espai d’emmagatzematge al núvol: 1Tb suficient
- APIs de tercers: No en fem servir
# 5. Requisits del Procés de Desenvolupament
- IDE’s: VScode , Miniconda3 (python)
- Extensions VSCode: python, python snippets
- Control de Versions: Git, GitHub
- Mètode de desenvolupament: Seguir una metodologia àgil com Scrum per iterar i validar funcionalitats amb usuaris reals.
- Proves de qualitat (QA): Tests de proves Unitàries