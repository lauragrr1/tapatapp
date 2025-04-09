import mysql.connector
from mysql.connector import Error

try:
    # Establim la connexió
    connection = mysql.connector.connect(
        host='localhost',
        database='tapatapp',
        user='root',
        password='root'
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connexió establerta amb MySQL Server versió", db_info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("Estàs connectat a la base de dades:", record[0])

except Error as e:
    print("Error mentre es connectava a MySQL:", e)

finally:
    # Tanquem la connexió
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexió amb MySQL tancada.")
