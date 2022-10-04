import mysql.connector


try:
    conexion = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        password = 'g15566757',
        db = 'prueba_1'
    )
    if conexion.is_connected():
        print("la conexion fue exitosa")
        informacion_del_servidor = conexion.get_server_info()
        print (informacion_del_servidor)

except:
    print ("No se conecto")

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion se cerro")
