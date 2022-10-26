from unittest.util import _count_diff_all_purpose
import mysql.connector
from rich import print

class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = '127.0.0.1',
                port = 3306,
                user = 'root',
                password = 'g15566757',
                db = 'disqueria1'

            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)

    def __str__(self):
        datos = self.consulta_albumes_por_artista()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def __str__(self):
        datos = self.consulta_albumes_por_genero()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_albumes_por_artista (self):
        cur = self.conexion.cursor()
        cur.execute ("SELECT cod_album, album.nombre, interprete.nombre, interprete.apellido FROM album, interprete WHERE album.id_interprete = interprete.id_interprete ORDER BY interprete.apellido desc")
        datos = cur.fetchall()
        cur.close()
        return datos

    def consulta_albumes_por_genero (self):
        cur = self.conexion.cursor()
        cur.execute ("SELECT genero.nombre, cod_album, album.nombre, interprete.nombre, interprete.apellido FROM album, interprete, genero WHERE album.id_interprete = interprete.id_interprete AND album.id_genero = genero.id_genero ORDER BY genero.nombre asc ")
        datos = cur.fetchall()
        cur.close()
        return datos

    def insertar_album(self,album):
        if self.conexion.is_connected():

            cur = self.conexion.cursor()
            sentenciaSQL = "insert into album values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            data = (
            album.getCod_album(),
            album.getNombre(),
            album.getId_interprete(),
            album.getId_genero(),
            album.getCant_temas(),
            album.getId_discografica(),
            album.getId_formato(),
            album.getFec_lanzamiento(),
            album.getPrecio(),
            album.getCantidad(),
            album.getCaratula())

            cur.execute(sentenciaSQL,data)
            self.conexion.commit()
            self.conexion.close()
            print("Álbum agregado correctamente")

    def eliminar_album(self, cod_album):
        cur = self.conexion.cursor()
        sentenciaSql = f"DELETE FROM album WHERE cod_album = {cod_album}"
        cur.execute(sentenciaSql)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n, print("Album eliminado correctamente")

    def modificar_album_nombre(self,nombre, cod_album):
        cur = self.conexion.cursor()
        sentenciaSql = "UPDATE album SET nombre = %s WHERE cod_album = %s"
        data = (nombre, cod_album)
        cur.execute(sentenciaSql, data)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n, print("Nombre del album modificado correctamente"), print(f"Nuevo nombre: {nombre}")

    def modificar_album_precio(self,precio, cod_album):
        cur = self.conexion.cursor()
        sentenciaSql = "UPDATE album SET precio = %s WHERE cod_album = %s"
        data = (precio, cod_album)
        cur.execute(sentenciaSql, data)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n, print("Precio del album modificado correctamente"), print(f"Nuevo precio: {precio}")
    
    def modificar_album_cantidad(self,cantidad, cod_album):
        cur = self.conexion.cursor()
        sentenciaSql = "UPDATE album SET cantidad = %s WHERE cod_album = %s"
        data = (cantidad, cod_album)
        cur.execute(sentenciaSql, data)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n, print("Stock del album modificado correctamente"), print(f"Nuevo stock: {cantidad}")

    def insertar_interprete(self,interprete):
        if self.conexion.is_connected():
            cur = self.conexion.cursor()
            sentenciaSQL = "INSERT into interprete values(null,%s,%s,%s,%s)"
            data = (
            interprete.getNombre(),
            interprete.getApellido(),
            interprete.getNacionalidad(),
            interprete.getFoto()
            )
            cur.execute(sentenciaSQL,data)
            self.conexion.commit()
            self.conexion.close()

    def busqueda_por_nombre_album(self, album):
        cur = self.conexion.cursor()
        sentenciaSql = "SELECT cod_album, nombre, precio, cantidad FROM album WHERE nombre like %s"
        data = (
            album.getNombre(),
        )
        cur.execute(sentenciaSql, data)
        datos = cur.fetchone()
        self.conexion.close()
        return datos, print(datos)

    def listar_interpretes(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT * FROM interprete"
        cursor.execute(sentenciaSQL)
        resultados = cursor.fetchall()
        return resultados

    def listar_genero(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT * FROM genero"
        cursor.execute(sentenciaSQL)
        resultados = cursor.fetchall()
        return resultados

    def listar_discografica(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT * FROM discografica"
        cursor.execute(sentenciaSQL)
        resultados = cursor.fetchall()
        return resultados

    def listar_formato(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT * FROM formato"
        cursor.execute(sentenciaSQL)
        resultados = cursor.fetchall()
        return resultados

    def listar_album(self):
        cur = self.conexion.cursor()
        sentenciaSql = "SELECT id_album, cod_album, nombre, precio, cantidad FROM album"
        cur.execute(sentenciaSql)
        resultados = cur.fetchall()
        return resultados

# con = Conectar()
# con.listar_formato()




#-----------------------------------------------------------------------------------------------------------------------------------------------
class Interprete():     

    def __init__(self,id_interprete,nombre,apellido,nacionalidad,foto) -> None:
        self.id_interprete = id_interprete
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.foto = foto

    def getId_Interprete(self):
        return self.id_interprete
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getNacionalidad(self):
        return self.nacionalidad
    def getFoto(self):
        return self.foto

    def setId_Interprete(self,idInterprete):
        self.id_interprete = idInterprete
    def setNombre(self,nombre):
        self.nombre = nombre
    def setApellido(self,apellido):
        self.apellido = apellido
    def setNacionalidad(self,nacionalidad):
        self.nacionalidad = nacionalidad
    def setFoto(self,foto):
        self.foto = foto

    def __str__(self) -> str:
        return str(self.id_interprete)+' '+self.nombre+' '+self.apellido+' '+self.nacionalidad+' '+self.foto

#---------------------------------------------------------------------------------------

class Genero():
    def __init__(self,id_genero,nombre) -> None:
        self.id_genero = id_genero
        self.nombre = nombre

    def __str__(self) -> str:
        return str(self.id_genero)+' '+self.nombre

    def getId_genero(self):
        return self.getId_genero
    def getNombre(self):
        return self.nombre

    def setId_genero(self,id_genero):
        self.id_genero = id_genero
    def setNombre(self,nombre):
        self.nombre = nombre


#---------------------------------------------------------------------------------------

class Discografica():
    def __init__(self,id_discografica,nombre) -> None:
        self.id_discografica = id_discografica
        self.nombre = nombre

    def __str__(self) -> str:
        return str(self.id_discografica)+' '+self.nombre

    def getId_discografica(self):
        return self.id_discografica
    def getNombre(self):
        return self.nombre
    
    def setId_discografica(self,id_discografica):
        self.id_discografica = id_discografica
    def setNombre(self,nombre):
        self.nombre = nombre


#---------------------------------------------------------------------------------------

class Formato():
    def __init__(self,id_formato,tipo) -> None:
        self.id_formato = id_formato
        self.tipo = tipo

    def __str__(self) -> str:
        return str(self.id_formato)+' '+self.tipo

    def getId_formato(self):
        return self.id_formato
    def getTipo(self):
        return self.tipo

    def setId_formato(self,id_formato):
        self.id_formato = id_formato
    def setTipo(self,tipo):
        self.tipo = tipo

#---------------------------------------------------------------------------------------

class Tema():
    def __init__(self,id_tema,titulo,duracion,autor,compositor,cod_album,id_interprete) -> None:
        self.id_tema = id_tema
        self.titulo = titulo
        self.duracion = duracion
        self.autor = autor
        self.compositor = compositor
        self.cod_album = cod_album
        self.id_interprete = id_interprete

    def getId_tema(self):
        return self.id_tema
    def getTiulo(self):
        return self.titulo
    def getDuracion(self):
        return self.duracion
    def getAutor(self):
        return self.autor
    def getCompositor(self):
        return self.compositor
    def getCod_album(self):
        return self.cod_album
    def getId_interprete(self):
        return self.id_interprete

    def setId_tema(self,id_tema):
        self.id_tema = id_tema
    def setTitulo(self,titulo):
        self.titulo = titulo
    def setDuracion(self,duracion):
        self.duracion = duracion
    def setAutor(self,autor):
        self.autor = autor
    def setCompositor(self,compositor):
        self.compositor = compositor
    def setCod_album(self,cod_album):
        self.cod_album = cod_album
    def setId_interprete(self,id_interprete):
        self.id_interprete = id_interprete

    def __str__(self) -> str:
        return str(self.id_tema)+' '+self.titulo+' '+str(self.duracion)+' '+self.autor+' '+self.compositor+' '+str(self.cod_album)+' '+str(self.id_interprete)
    


#---------------------------------------------------------------------------------------

class AlbumParaBusqueda():
    def __init__(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre

class Album():
    def __init__(self,id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula) -> None:
        self.id_album = id_album
        self.cod_album = cod_album
        self.nombre = nombre
        self.id_interprete = id_interprete
        self.id_genero = id_genero
        self.cant_temas = cant_temas
        self.id_discografica = id_discografica
        self.id_formato = id_formato
        self.fec_lanzamiento = fec_lanzamiento
        self.precio = precio
        self.cantidad = cantidad
        self.caratula = caratula

    def getId_album(self):
        return self.id_album
    def getCod_album(self):
        return self.cod_album
    def getNombre(self):
        return self.nombre
    def getId_interprete(self):
        return self.id_interprete
    def getId_genero(self):
        return self.id_genero
    def getCant_temas(self):
        return self.cant_temas
    def getId_discografica(self):
        return self.id_discografica
    def getId_formato(self):
        return self.id_formato
    def getFec_lanzamiento(self):
        return self.fec_lanzamiento
    def getPrecio(self):
        return self.precio
    def getCantidad(self):
        return self.cantidad
    def getCaratula(self):
        return self.caratula

    def setId_album(self,id_album):
        self.id_album = id_album
    def setCod_album(self,cod_album):
        self.cod_album = cod_album
    def setNombre(self,nombre):
        self.nombre = nombre
    def setId_interprete(self,id_interprete):
        self.id_interprete = id_interprete
    def setId_genero(self,id_genero):
        self.id_genero = id_genero
    def setCant_temas(self,cant_temas):
        self.cant_temas = cant_temas
    def setId_discografica(self,id_discografica):
        self.id_discografica = id_discografica
    def setId_formato(self,id_formato):
        self.id_formato = id_formato
    def setFec_lanzamiento(self,fec_lanzamiento):
        self.fec_lanzamiento = fec_lanzamiento
    def setPrecio(self,precio):
        self.precio = precio
    def setCantidad(self,cantidad):
        self.cantidad = cantidad
    def setCaratula(self,caratula):
        self.caratula = caratula

    def __str__(self) -> str:
        return str(self.id_album) +' '+ str(self.cod_album) +' '+ self.nombre +' '+ str(self.id_interprete) +' '+ str(self.id_genero) +' '+ str(self.cant_temas) +' '+ str(self.id_discografica) +' '+ str(self.id_formato) +' '+ self.fec_lanzamiento +' '+ str(self.precio) +' '+ str(self.cantidad) +' '+ self.caratula


# con = Conectar()
# con.eliminar_album(1234567)
