import mysql.connector

def connect_and_list_users():
    try:
        # Conexión a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos.")

            # Crear un cursor para ejecutar consultas
            cursor = connection.cursor(dictionary=True)

            # Consulta para obtener los datos de la tabla User
            query = "SELECT * FROM User"
            cursor.execute(query)

            # Obtener y mostrar los resultados
            users = cursor.fetchall()
            if users:
                print("Datos de la tabla User:")
                for user in users:
                    print(f"ID: {user['id']}, Username: {user['username']}, Email: {user['email']}")
            else:
                print("La tabla User está vacía.")

            # Cerrar el cursor
            cursor.close()

    except mysql.connector.Error as err:
        print(f"Error al conectar o consultar la base de datos: {err}")

    finally:
        # Cerrar la conexión
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Conexión cerrada.")

# Ejecutar la función
if __name__ == "__main__":
    connect_and_list_users()