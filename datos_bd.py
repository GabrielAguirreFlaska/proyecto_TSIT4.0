import mysql.connector


try:
    conexion = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        password = 'g15566757',
        db = 'disqueria'
    )
    if conexion.is_connected():
        print("la conexion fue exitosa")

        cursor = conexion.cursor()
        cursor.execute("select * from tema")
        lista = cursor.fetchall()

        for dato in lista:
            print (dato)


except mysql.connector.Error as ex:
    print ("No se conecto")
    print (ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion se cerro")