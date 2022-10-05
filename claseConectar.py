import mysql.connector

class Conectar():

    def __init__(self) -> None:
        try: 
            self.conexion = mysql.connector.connect(
                host = '127.0.0.1',
                port = 3306,
                user = "root",
                password = "g15566757",
                db = "disqueria"
            )
            print("connection established")
        except mysql.connector.Error as descripcionError:
            print("Error connecting to database", descripcionError)

    def ListarAlbumes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT cod_album, album.nombre, interprete.nombre, interprete.apellido, genero.nombre, discografica.nombre, precio, cantidad, formato.tipo FROM album, interprete, discografica, formato, genero WHERE album.id_interprete = interprete.id_interprete AND album.id_discografica = discografica.id_discografica AND album.id_formato = formato.id_formato AND album.id_genero = genero.id_genero ORDER By album.id_interprete")
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as descripcionErrorListarAlbumes:
                print("Error connecting to database", descripcionErrorListarAlbumes)

#Listado de albumes disponibles por artista, en orden alfabetico

#con = Conectar()

#for album in con.ListarAlbumes():
#    print ("Album:", album[1] + ". " + "Interprete:", album[2])

