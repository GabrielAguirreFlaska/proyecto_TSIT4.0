import modelo as mo

def listar_albumes_por_artista():
    con = mo.Conectar()
    listado = con.consulta_albumes_por_artista()
    for album in listado:
        print(' ',"Artista:",album[2],album[3],"\n","Codigo del album:",album[0],"\n","Nombre del album:",album[1])
        print("\n")
    input("Presione ENTER para continuar")

#listar_albumes_por_artista()


def listar_albumes_por_genero():
    con = mo.Conectar()
    listado = con.consulta_albumes_por_genero()
    for genero in listado:
        print(' ', "Genero:",genero[0],"\n","Artista:",genero[3],genero[4],"\n","Album:",genero[2],"\n","Codigo del album:",genero[1])
        print("\n")
    input("Presiones ENTER para continuar")

#listar_albumes_por_genero()


def ingresar_interprete():
    con = mo.Conectar()
    print("Estos son los interpretes que ya existen: ","\n")
    listado_de_interpretes = con.listar_interpretes()
    for interprete in listado_de_interpretes:
        print(' ',"Nombre:",interprete[1],interprete[2],"\n","Nacionalidad:",interprete[3])
        print("\n")
    print("Ingrese los siguientes datos de su interprete: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    nacionalidad = input("Nacionalidad: ")
    foto = input("Ingrese la url de la foto de su interprete: ")
    
    nuevo_interprete = mo.Interprete(0, nombre,apellido,nacionalidad,foto)
    con.insertar_interprete(nuevo_interprete)
    con.conexion.close()
    print(f"El interprete {nombre},' '{apellido} fue ingresado correctamente.")
    print("Presione ENTER para continuar")

#ingresar_interprete()

def buscar_por_album():
    con = mo.Conectar()
    nombre = input("Ingrese el nombre del album que desea buscar: ")
    nombre_album = mo.AlbumParaBusqueda(nombre)
    con.busqueda_por_nombre_album(nombre_album)
    con.conexion.close()
    print("Presiones ENTER para continuar")

#buscar_por_album()

def agregar_album():
    con = mo.Conectar()
    cod_album = int(input("\nIngrese el código del nuevo Álbum: "))
    nombre = input("Ingrese el nombre del álbum: ")
    print("\nIntérpretes Disponibles:")
    listado_de_interpretes = con.listar_interpretes()
    for listado in listado_de_interpretes:
        print(listado)
    id_interprete = int(input("\nIngrese el ID del Intérprete: "))
    
    print("\nGéneros disponibles:")
    listado_de_generos = con.listar_genero()
    for g in listado_de_generos:
        print(g)
    id_genero = int(input("\nIngrese el ID del Género: "))
    cant_temas = int(input("\nIngrese la cantidad de temas que contiene el album: "))

    print("\nDiscográficas disponibles:")
    listado_de_discograficas = con.listar_discografica()
    for d in listado_de_discograficas:
        print(d)
    id_discografica = int(input("\nIngrese el ID de la discografica: "))

    print("\nFormatos disponibles:")
    listado_de_formatos = con.listar_formato()
    for f in listado_de_formatos:
        print(f)
    id_formato = int(input("\nIngrese el ID del formato: "))

    fec_lanzamiento = input("\nIngrese la Fecha de Lanzamiento del album (aaaa-mm-dd): ")
    precio = float(input("\nIngrese su precio: "))
    cantidad = float(input("\nIngrese el stock disponible de este álbum: "))
    caratula = input("\nIngrese la dirección web de la Carátula: ")

    nuevoAlbum = mo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)
    con.insertar_album(nuevoAlbum)
    input("Presione ENTER para continuar")

#agregar_album()

def baja_album():
    con = mo.Conectar()
    print("Albumes disponibles:")
    listado_de_albumes = con.listar_album()
    for listado in listado_de_albumes:
        print(' ', "ID del album:",listado[0], "Codigo del album: ",listado[1], ".", "Nombre del album: ", listado[2] )
    album = input("Ingrese codigo del album que desea eliminar: ")
    con.eliminar_album(album)

#baja_album()

def modificar_nombre_album():
    con = mo.Conectar()
    print("Albumes disponibles:")
    listado_de_albumes = con.listar_album()
    for listado in listado_de_albumes:
        print(' ', "ID del album:",listado[0], "Codigo del album: ",listado[1], ".", "Nombre del album: ", listado[2] )
    cod_album = int(input("Ingrese el codigo del album del cual quiere modificar su nombre: "))
    nombre = input("Ingrese el nuevo nombre del album: ")
    con.modificar_album_nombre(nombre, cod_album)

# modificar_nombre_album()

def modificar_precio_album():
    con = mo.Conectar()
    print("Albumes disponibles:")
    listado_de_albumes = con.listar_album()
    for listado in listado_de_albumes:
        print(' ', "ID del album:",listado[0], "Codigo del album: ",listado[1], ".", "Nombre del album: ", listado[2], ".", "Precio:",listado[3])
    cod_album = int(input("Ingrese el codigo del album del cual quiere modificar su precio: "))
    precio = input("Ingrese el nuevo precio del album: ")
    con.modificar_album_precio(precio, cod_album)

#modificar_precio_album()

def modificar_stock_album():
    con = mo.Conectar()
    print("Albumes disponibles:")
    listado_de_albumes = con.listar_album()
    for listado in listado_de_albumes:
        print(' ', "ID del album:",listado[0], "Codigo del album: ",listado[1], ".", "Nombre del album: ", listado[2], ".", "Stock:",listado[4])
    cod_album = int(input("Ingrese el codigo del album del cual quiere modificar su stock: "))
    cantidad = input("Ingrese el nuevo stock para este album: ")
    con.modificar_album_cantidad(cantidad, cod_album)

#modificar_stock_album()