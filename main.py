canciones = []
tonicas_validas = ["A", "B", "C", "D", "E", "F", "G"]

while True:
    titulo_valor = input("Título de la canción: ")

    if len(titulo_valor.strip()) > 0:
        break
    else:
        print("Este campo no puede quedar vacio")

artista_valor = input("Artista de la canción: ")

if artista_valor.strip() == "":
    artista_valor = "Desconocido"
else:
    artista_valor = artista_valor.strip()

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
    
duracion_valor = (min_valor * 60) + seg_valor

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

while True:
    try:
        dificultad_valor = int(input("Dificultad (1) Fácil (2) Media (3) Difícil: "))

        if dificultad_valor == 1 or dificultad_valor == 2 or dificultad_valor == 3:
            break
        else:
            print("Selecciona únicamente 1, 2 o 3.")
    except ValueError:
        print("Debes escribir un número: 1, 2 o 3.")

if dificultad_valor == 1:
    dificultad_valor = "Fácil"
elif dificultad_valor == 2:
    dificultad_valor = "Media"
elif dificultad_valor == 3:
    dificultad_valor = "Difícil"

while True:
    youtube_valor = input( "Enlace de YouTube; deja vacío si no tienes: ")

    youtube_valor = youtube_valor.strip()

    if youtube_valor.startswith(("https://", "http://")):
        break
    elif youtube_valor == "":
        break
    else:
        print("Introduce una URL valida o deja el campo vacio")

while True:
    tab_valor = input("Enlace de tablatura; deja vacío si no tienes: ")

    tab_valor = tab_valor.strip()

    if tab_valor.startswith(("https://", "http://")):
        break
    elif tab_valor == "":
        break
    else:
        print("Introduce una URL valida o deja el campo vacio")

cancion = {'titulo': titulo_valor.strip(), 
            'artista':artista_valor, 
            'duracion_segundos':duracion_valor, 
            'afinacion': f"{tonica_valor.upper()}{tipo_alteracion} {tipo_afinacion}", 
            'dificultad':dificultad_valor, 
            'youtube': youtube_valor, 
            'tablatura': tab_valor }

canciones.append(cancion)

print(canciones)
   