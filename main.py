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

canciones = cargar_canciones()
while True:
    try:
        print(" 1. Agregar canción \n 2. Ver canción \n 3. Salir ")
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
        print("Hasta luego")
        break
    else:
        print("Ese es un número no valido")
        print("-" * 10)



   