1- (testunitaris.md) Què són els tests unitaris?
Els tests unitaris són proves automatitzades que comproven el funcionament correcte de les unitats més petites d'un programa, com ara funcions o mòduls. Això permet detectar errors en etapes inicials del desenvolupament i facilita el manteniment del codi.


2- (testunitaris.md) Fes una recerca de llibreries de test amb Python.  Com funciona específicament la llibreria unittest de Python?
Python disposa de diverses llibreries per realitzar tests unitaris. Algunes de les més populars són:

unittest: Inclosa a la llibreria estàndard de Python, proporciona eines per escriure i executar tests.

pytest: Una llibreria més flexible i avançada que suporta funcionalitats modernes.

nose2: Un successor de nose amb una integració senzilla.

Sobre unittest, funciona definint classes que hereten de unittest.TestCase. A cada classe s'hi poden afegir mètodes que comencen amb "test_" per definir proves, i assertions per verificar el comportament esperat.


3-  (prototip3/testsuma.py) Exercici exemple test.
Creació i execució d’un test senzill  amb Python per exemple testejar una funció de suma. Genera un fitxer python que testeji aquesta funció.

def suma(a, b):
    """Retorna la suma de dos nombres."""
    return a + b

4- (prototip3/testfuncions.py) Exercici exemple varies  funcions.
Testeja més funcions, afegeix una resta i una divisió (que retorni un error quan la divisió és per 0)  

def resta(a, b):
    """Retorna la resta de dos nombres."""
    return a - b

def divideix(a, b):
    """Retorna la divisió de dos nombres. Retorna 'Error' si b és 0."""
    if b == 0:
        return "Error: divisió per zero"
    return a / b

5-  (testunitaris.md) Fes una Llista de les assertions més importants en unittest i explica per a que  serveixen

6-  (prototip3/testBackend.py)  Fes els tests Unitaris dels teus DAO i webservice del prototip 2 que tens a la carpeta prototip 3
