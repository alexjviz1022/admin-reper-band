import json

def cargar_canciones():
    try:
        with open("canciones.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_canciones():
    with open("canciones.json", "w") as archivo:
        json.dump(canciones, archivo, indent=4)

def pedir_titulo():
    while True:
        titulo = input("Título de la canción: ")

        if len(titulo.strip()) > 0:
            return titulo.strip()
        else:
            print("Este campo no puede quedar vacio")

def pedir_artista():
    artista = input("Artista de la canción: ")

    if artista.strip() == "":
        return "Desconocido"
    else:
        return artista.strip()

def pedir_duracion():
    
    while True:
        try:
            min_valor = int(input("Duración — minutos: "))

            if min_valor >= 0 and min_valor <= 30:
                break
            elif min_valor > 30:
                print("No creo que sea As Slow as Possible, solo canciones de hasta 30 minutos o menos")
            else: 
                print("Los minutos no pueden ser negativos")
        except ValueError:
            print("Solo se aceptan numeros enteros")

    while True:
        try:
            seg_valor = int(input("Duración — segundos: "))

            if seg_valor >= 0 and seg_valor <= 59:
                break
            else: 
                print("Solo números entre 0 y 59")
        except ValueError:
            print("Solo se aceptan numeros enteros")
        
    duracion = (min_valor * 60) + seg_valor

    return duracion

def pedir_afinacion():

    tonicas_validas = ["A", "B", "C", "D", "E", "F", "G"]

    while True:
        print("En caso de que la tonalidad tenga alteración se preguntara despues")
        tonica_valor = input("Tónica de la afinación: ")
        tonica_valor = tonica_valor.strip()

        if tonica_valor.upper() in tonicas_validas:
            break
        else: 
            print("Por favor introduzca una tónica valida")
            print("Ejemplo: C, D, E, F, G, A, B")

    while True:
        try:
            tipo_alteracion = int(input("Alteración: (0) Ninguna (1) Sostenido # (2) Bemol b: "))

            if tipo_alteracion == 0 or tipo_alteracion == 1 or tipo_alteracion == 2:
                break
            else:
                print("Selecciona únicamente 0, 1 o 2.")
        except ValueError:
            print("Debes escribir un número: 0, 1 o 2.")

    if tipo_alteracion == 0:
        tipo_alteracion = ""
    elif tipo_alteracion == 1:
        tipo_alteracion = "#"
    elif tipo_alteracion == 2:
        tipo_alteracion = "b"

    while True:
        try:
            tipo_afinacion = int(input("Tipo de afinación: (1) Estándar o (2) Drop: "))

            if tipo_afinacion == 1 or tipo_afinacion == 2:
                break
            else:
                print("Selecciona únicamente 1 o 2.")
        except ValueError:
            print("Debes escribir un número: 1 o 2.")

    if tipo_afinacion == 1:
        tipo_afinacion = "Estándar"
    elif tipo_afinacion == 2:
        tipo_afinacion = "Drop"

    if tipo_afinacion == "Drop":
        orden = f"{tipo_afinacion} {tonica_valor.upper()}{tipo_alteracion}"
    else:
        orden = f"{tonica_valor.upper()}{tipo_alteracion} {tipo_afinacion}"

    return orden

def pedir_dificultad():
    while True:
        try:
            dificultad = int(input("Dificultad (1) Fácil (2) Media (3) Difícil: "))

            if dificultad == 1 or dificultad == 2 or dificultad == 3:
                break
            else:
                print("Selecciona únicamente 1, 2 o 3.")
        except ValueError:
            print("Debes escribir un número: 1, 2 o 3.")

    if dificultad == 1:
        dificultad = "Fácil"
    elif dificultad == 2:
        dificultad = "Media"
    elif dificultad == 3:
        dificultad = "Difícil"
    return dificultad

def pedir_enlace(texto_enlace):

    while True:
        enlace_valor = input(texto_enlace)

        enlace_valor = enlace_valor.strip()

        if enlace_valor.startswith(("https://", "http://")):
            return enlace_valor
        elif enlace_valor == "":
            return enlace_valor
        else:
            print("Introduce una URL valida o deja el campo vacio")

def agregar_cancion():
    titulo_valor = pedir_titulo()

    artista_valor = pedir_artista()

    duracion_valor = pedir_duracion()

    tipo_afinacion = pedir_afinacion()

    dificultad_valor = pedir_dificultad()

    cancion_enlace_valor = pedir_enlace("Enlace de la canción (video YouTube o Spotify); deja vacío si no tienes: ")

    tabs_enlace_valor = pedir_enlace("Enlace de tablatura; deja vacío si no tienes: ")


    cancion = {'titulo': titulo_valor, 
                'artista':artista_valor, 
                'duracion_total':duracion_valor, 
                'afinacion':tipo_afinacion, 
                'dificultad':dificultad_valor, 
                'enlace_cancion': cancion_enlace_valor, 
                'enlace_tablatura': tabs_enlace_valor }

    canciones.append(cancion)

def mostrar_canciones():
    for num_canciones, cancion in enumerate(canciones, start=1):
        minutos, segundos = divmod(cancion['duracion_total'], 60)
        print(
            f"{num_canciones}. {cancion['titulo']}\n"
            f"   Artista: {cancion['artista']}\n"
            f"   Duración: {minutos}:{segundos:02d}\n"
            f"   Afinación: {cancion['afinacion']}\n"
            f"   Dificultad: {cancion['dificultad']}\n"
        )

def mostrar_lista_canciones():    
    for num_canciones, cancion in enumerate(canciones, start=1):
        print(
            f"{num_canciones}. {cancion['titulo']}\n"
                )

def editar_cancion():
    print("0. cancelar\n")
    mostrar_lista_canciones()
    while True:
        try:
            eleccion_usuario = int(input("¿Que canción quieres editar? Solo puedes elegir el número de la canción: "))
            if eleccion_usuario >= 1 and eleccion_usuario <= len(canciones):
                break
            elif eleccion_usuario == 0:
                print("-" * 10)
                return
            else:
                print("Solo puedes elegir las canciones que esten agregadas")
        except ValueError:
            print("Solo se permiten números enteros")


    indice = eleccion_usuario - 1

    while True:
        try:
            modificacion_exacta = int(input("Elije uno de los números disponibles\n0.Cancelar\n1.Titulo\n2.Artista\n3.Duración\n4.Afinación\n5.Dificultad\n6.Enlace a la canción\n7.Tablaturas\n¿Que quieres modificar? "))
            if modificacion_exacta == 1:
                print("Realiza los cambios al titulo")
                canciones[indice]["titulo"] = pedir_titulo()
                break

            elif modificacion_exacta == 2:
                print("Realiza los cambios al artista")
                canciones[indice]["artista"] = pedir_artista()
                break

            elif modificacion_exacta == 3:
                print("Realiza los cambios a la duración")
                canciones[indice]["duracion_total"] = pedir_duracion()
                break

            elif modificacion_exacta == 4:
                print("Realiza los cambios de la afinación")
                canciones[indice]["afinacion"] = pedir_afinacion()
                break
            
            elif modificacion_exacta == 5:
                print("Realiza los cambios a la dificultad")
                canciones[indice]["dificultad"] = pedir_dificultad()
                break
            elif modificacion_exacta == 6:
                print("Realiza los cambios al enlace de YouTube")
                canciones[indice]["enlace_cancion"] = pedir_enlace("Enlace de la canción; deja vacío si no tienes: ")
                break
                        
            elif modificacion_exacta == 7:
                print("Realiza los cambios al enlace de las tablaturas")
                canciones[indice]["enlace_tablatura"] = pedir_enlace("Enlace de tablatura; deja vacío si no tienes: ")
                break
            elif modificacion_exacta == 0:
                print("-" * 10)
                return

            else:
                print("Solo se permiten los números de la lista")
        except ValueError:
            print("Solo números enteros")
    guardar_canciones()
    print("-" * 10)
    print("CAMBIOS LISTOS")
    print(canciones[indice])
    print("-" * 10)

def eliminar_cancion():
    print("0. cancelar\n")
    mostrar_lista_canciones()
    while True:
        try:
            eleccion_usuario_eliminacion = int(input("¿Que canción quieres eliminar? Solo puedes elegir el número de la canción: "))
            if eleccion_usuario_eliminacion >= 1 and eleccion_usuario_eliminacion <= len(canciones):
                break
            elif eleccion_usuario_eliminacion == 0:
                return
            else:
                print("Solo puedes elegir las canciones que esten agregadas")
        except ValueError:
            print("Solo se permiten números enteros")


    indice = eleccion_usuario_eliminacion - 1

    while True:
        try:
            eleccion_final_eliminar = int(input(f"¿Estas seguro de querer eliminar: {canciones[indice]["titulo"]}?\n1.Si\n2.No\n"))
            if eleccion_final_eliminar == 1:
                canciones.pop(indice)
                guardar_canciones()
                print("Canción eliminada con exito")
                print("-" * 10)
                break
            elif eleccion_final_eliminar == 2:
                return
            else:
                print("Solo puedes elegir entre esas dos opciones:")
        except ValueError:
            print("Solo números enteros")

canciones = cargar_canciones()
while True:
    try:
        print(" 1. Agregar canción \n 2. Ver canción \n 3. Editar \n 4. Eliminar \n 5. Salir ")
        usuario_eleccion = int(input("Selecciona una opción del menu: "))
    except ValueError:
        print("Solo se permiten los números antes indicados")
        print("-" * 10)
        continue

    if usuario_eleccion == 1:
        agregar_cancion()
        guardar_canciones()
        print("-" * 10)
    elif usuario_eleccion == 2:
        if canciones == []:
            print("Aun no hay canciones agregadas")
            print("-" * 10)
        else:
            print("---CANCIONES---")
            mostrar_canciones()
            print("-" * 10)
    elif usuario_eleccion == 3:
        if canciones == []:
            print("Aun no hay canciones agregadas")
            print("-" * 10)
        else:
            editar_cancion()         
    elif usuario_eleccion == 4:
        if canciones == []:
            print("Aun no hay canciones agregadas")
            print("-" * 10)
        else:
            eliminar_cancion()    
    elif usuario_eleccion == 5:
        print("Hasta luego")
        break
    else:
        print("Ese es un número no valido")
        print("-" * 10)



   