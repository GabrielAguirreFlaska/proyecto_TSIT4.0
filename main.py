import control as con

while True:
    print("\n+-------------------------------------------+")
    print("|         DISQUERÍA FORMOSA MUSICAL         |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n")
    print("1 - DAR DE ALTA UN ÁLBUM")
    print("2 - DAR DE BAJA UN ALBUM")
    print("3 - MODIFICAR EL NOMBRE DE UN ALBUM")
    print("4 - MODIFICAR EL PRECIO DE UN ALBUM")
    print("5 - MODIFICAR EL STOCK DE UN ALBUM")
    print("6 - LISTADO DE ÁLBUMES POR ARTISTAS")
    print("7 - LISTADO DE ÁLBUMES POR GÉNERO MUSICAL")
    print("8 - INSERTAR INTERPRETE")
    print("9 - BUSQUEDA POR NOMBRE DE ALBUM")
    print("10 - SALIR")
    print("\n")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        con.agregar_album()
    elif opcion == 2:
        con.baja_album()
    elif opcion == 3:
        con.modificar_nombre_album()
    elif opcion == 4:
        con.modificar_precio_album()
    elif opcion == 5:
        con.modificar_stock_album()
    elif opcion == 6:
        con.listar_albumes_por_artista()
    elif opcion == 7:
        con.listar_albumes_por_genero()
    elif opcion == 8:
        con.ingresar_interprete()
    elif opcion == 9:
        con.buscar_por_album()
    elif opcion == 10:
        break
    else:
        print("¡Opción incorrecta!")
        print("Preciones ENTER para volver al menu")

