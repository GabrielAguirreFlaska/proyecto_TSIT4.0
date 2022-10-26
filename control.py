import modelo as mo
from rich import print
from rich.console import Console




console= Console()

def listar_albumes_por_artista():
    con = mo.Conectar()
    listado = con.consulta_albumes_por_artista()
    for album in listado:
        console.print(" ", "Artista:",album[2],album[3], style=("bold red"))
        console.print(' ',"Codigo del album:",album[0], style=("bold"))
        console.print(" ","Nombre del album:",album[1], style=("bold green"))
        print("\n")
    input("Presione ENTER para continuar")

#listar_albumes_por_artista()


def listar_albumes_por_genero():
    con = mo.Conectar()
    listado = con.consulta_albumes_por_genero()
    for genero in listado:
        console.print(' ', "Genero:",genero[0], style=("bold red"))
        console.print(" ", "Artista:",genero[3],genero[4], style=(" bold white"))
        console.print(" ", "Album:",genero[2], style=("bold green"))
        console.print(' ', "Codigo del album:",genero[1], style=("bold white"))
        print("\n")
    input("Presiones ENTER para continuar")


#listar_albumes_por_genero()


def ingresar_interprete():
    con = mo.Conectar()
    console.print("Estos son los interpretes que ya existen: ","\n", style=("bold red"))
    print("\n")
    listado_de_interpretes = con.listar_interpretes()
    for interprete in listado_de_interpretes:
        console.print(' ', "Nombre:",interprete[1],interprete[2],style=("bold green"))
        console.print(" ", "Nacionalidad:",interprete[3], style=("bold white"))
        print("\n")
    console.print("Ingrese los siguientes datos de su interprete: ", style=("bold red"))
    print("\n")
    console.print("Nombre:",style=("bold blue"))
    nombre = input("-> ")
    print("\n")
    console.print("Apellido:",style=("bold blue"))
    apellido = input("-> ")
    print("\n")
    console.print("Nacionalidad:",style=("bold blue"))
    nacionalidad = input("->")
    print("\n")
    console.print("Ingrese la url de la foto de su interprete: ", style=("bold blue"))
    foto = input("-> ")
    
    nuevo_interprete = mo.Interprete(0, nombre,apellido,nacionalidad,foto)
    con.insertar_interprete(nuevo_interprete)
    con.conexion.close()
    print("\n")
    console.print(f"El interprete '{nombre}, {apellido}' fue ingresado correctamente.", style=("bold green"))
    input("Presione ENTER para continuar")

#ingresar_interprete()

def buscar_por_album():
    con = mo.Conectar()
    console.print("Ingrese el nombre del album que desea buscar:",style=("bold blue"))
    nombre = input("->")
    nombre_album = mo.AlbumParaBusqueda(nombre)
    con.busqueda_por_nombre_album(nombre_album)
    con.conexion.close()
    input("Presiones ENTER para continuar")

#buscar_por_album()

def agregar_album():
    con = mo.Conectar()
    console.print("Ingrese el codigo del nuevo album:",style=("bold blue"))
    cod_album = int(input("->"))
    console.print("Ingrese el nombre del album:", style=("bold blue"))
    nombre = input("->")
    console.print("\nIntérpretes Disponibles:",style=("bold red"))
    print("\n")
    listado_de_interpretes = con.listar_interpretes()
    for listado in listado_de_interpretes:
        print(listado)
    console.print("Ingrese el ID del interprete:", style=("bold blue"))
    id_interprete = int(input("->"))
    
    console.print("\nGéneros disponibles:",style=("bold red"))
    print("\n")
    listado_de_generos = con.listar_genero()
    for g in listado_de_generos:
        print(g)
    console.print("Ingrese el ID del Genero:", style=("bold blue"))
    id_genero = int(input("->"))
    console.print("Ingrese la cantidad de temas que contiene el album:", style=("bold blue"))
    cant_temas = int(input("->"))
    print("\n")
    console.print("\nDiscográficas disponibles:",style=("bold red"))
    print("\n")
    listado_de_discograficas = con.listar_discografica()
    for d in listado_de_discograficas:
        print(d)
    console.print("Ingrese el ID de la discografica:", style=("bold blue"))
    id_discografica = int(input("->"))
    print("\n")
    console.print("\nFormatos disponibles:",style=("bold red"))
    print("\n")
    listado_de_formatos = con.listar_formato()
    for f in listado_de_formatos:
        print(f)
    console.print("Ingrese el ID del formato:", style=("bold blue"))
    id_formato = int(input("->"))
    print("\n")
    console.print("Ingrese la fecha de lanzamiento del album (aaaa-mm-dd)",style=("bold blue"))
    fec_lanzamiento = input("->")
    print("\n")
    console.print("Ingrese el precio del nuevo album:",style=("bold blue"))
    precio = float(input("->"))
    print("\n")
    console.print("Ingrese el stock disponible para este album:", style=("bold blue"))
    cantidad = float(input("->"))
    print("\n")
    console.print("Ingrese la direccion web de la caratula: ", style=("bold blue"))
    caratula = input("->")
    print("\n")
    nuevoAlbum = mo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)
    con.insertar_album(nuevoAlbum)
    input("Presione ENTER para continuar")

#agregar_album()

def baja_album():
    con = mo.Conectar()
    console.print("Albumes disponibles:", style=("bold red"))
    print("\n")
    listado_de_albumes = con.listar_album()
    for listado in listado_de_albumes:
        console.print(" ", "ID del album:",listado[0])
        console.print(" ", "Codigo del album: ",listado[1], style=("bold red"))
        console.print(" ", "Nombre del album: ", listado[2], style=("bold green"))
        print("\n")
    console.print("Ingrese el codigo del album que desea eliminar:",style=("bold blue"))
    album = input("-> ")
    con.eliminar_album(album)
    input("Presione ENTER para continuar")

#baja_album()

def modificar_nombre_album():
    con = mo.Conectar()
    console.print("Albumes disponibles:", style=("bold red"))
    print("\n")
    listado_de_albumes = con.listar_album()
    for listado in listado_de_albumes:
        console.print(" ", "ID del album:",listado[0])
        console.print(" ", "Codigo del album: ",listado[1], style=("bold red"))
        console.print(" ", "Nombre del album: ", listado[2], style=("bold green"))
        print("\n")
    console.print("Ingrese el codigo del album del cual quiere modificar su nombre:", style=("bold blue"))
    cod_album = int(input("-> "))
    print("\n")
    console.print("Ingrese el nuevo nombre del album:",style=("bold blue"))
    nombre = input("-> ")
    print("\n")
    con.modificar_album_nombre(nombre, cod_album)
    input("Presione ENTER para continuar")

# modificar_nombre_album()

def modificar_precio_album():
    con = mo.Conectar()
    console.print("Albumes disponibles:", style=("bold red"))
    print("\n")
    listado_de_albumes = con.listar_album()
    for listado in listado_de_albumes:
        console.print(" ", "ID del album:",listado[0])
        console.print(" ", "Codigo del album: ",listado[1], style=("bold red"))
        console.print(" ", "Nombre del album: ", listado[2], style=("bold green"))
        console.print(" ", "Precio: ", listado[3], style=("bold magenta"))
        print("\n")
    console.print("Ingrese el codigo del album del cual quiere modificar su precio:", style=("bold blue"))
    cod_album = int(input("-> "))
    print("\n")
    console.print("Ingrese el nuevo precio del album: ", style=("bold blue"))
    precio = input("-> ")
    print("\n")
    con.modificar_album_precio(precio, cod_album)
    input("Presione ENTER para continuar")

#modificar_precio_album()

def modificar_stock_album():
    con = mo.Conectar()
    console.print("Albumes disponibles:",style=("bold red"))
    print("\n")
    listado_de_albumes = con.listar_album()
    for listado in listado_de_albumes:
        console.print(" ", "ID del album:",listado[0])
        console.print(" ", "Codigo del album: ",listado[1], style=("bold red"))
        console.print(" ", "Nombre del album: ", listado[2], style=("bold green"))
        console.print(" ", "Stock: ", listado[4], style=("bold magenta"))
        print("\n")
    console.print("Ingrese el codigo del album del cual quiere modificar su stock:", style=("bold blue"))
    cod_album = int(input("-> "))
    print("\n")
    console.print("Ingrese el stock actual para este album:", style=("bold blue"))
    cantidad = input("-> ")
    print("\n")
    con.modificar_album_cantidad(cantidad, cod_album)
    input("Presione ENTER para continuar")

#modificar_stock_album()