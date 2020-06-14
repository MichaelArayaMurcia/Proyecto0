#----------- Proyecto 0 - Michael Araya Murcia - Jose Julian Araya Castillo -------
import json, random

def limpiarPantalla():
	
	print("\n" * 40)

def mensajeBienvenida():
    """
    Procedimiento que imprime un mensaje de bienvenida con la descripción y las reglas del juego.
    Entradas: Ninguna
    Salidas: Ninguna
    Restricciones: Ninguna
    """
    print(" %%%%%%  %%%%%   %%%%%%  %%  %%  %%%%%%   %%%% ")
    print("   %%    %%  %%    %%    %%  %%    %%    %%  %%")
    print("   %%    %%%%%     %%    %%  %%    %%    %%%%%%")
    print("   %%    %%  %%    %%     %%%%     %%    %%  %%")
    print("   %%    %%  %%  %%%%%%    %%    %%%%%%  %%  %%")
    print("        										  ")

    print("Descripción: Trivia es un juego en donde jugadores se reunen para ver quien sabe mas sobre un tema en especifico.")
    print("Reglas: ")
    print("1) Cada jugador debe responder 5 preguntas, durante 3 rondas \n   al final del juego el que haya acertado mas preguntas es el ganador.")
    print("----------------------------------------------------")

def cantidadJugadores():
    """
    Funcion que le pide al usuario la cantidad de jugadores que van a jugar y sus respectivos nombres.
    Entrada: Ninguna.
    Salida: La lista de jugadores que van a jugar.
    Restricciones: La cantidad de jugadores debe de ser un entero positivo.
    """
    aceptar = False

    listadejugadores = {}

    while not aceptar:
        cantidad = input("Ingrese cantidad de jugadores: ")

        if not cantidad.isnumeric():
            print("La cantidad tiene que ser un numero positivo.")
        elif cantidad.isnumeric() and int(cantidad) <= 0:
            print("La cantidad tiene que ser un numero positivo.")
        else:
            aceptar = True

    cantidad = int(cantidad)

    for i in range(0,cantidad):
        nombre = input("Ingrese el nombre del jugador " + str(i + 1) + ": ")
        listadejugadores["jugador"+str(i+1)] = {}
        listadejugadores["jugador"+str(i+1)]["nombre"] = nombre 
        listadejugadores["jugador"+str(i+1)]["puntuacion"] = 0

    return listadejugadores

def mostrarPuntuacion(listadejugadores):
    """
    Función que muestra en pantalla la lista de jugadores con sus puntuaciones.
    Entrada: Un diccionario con los jugadores.
    Salidas: Ninguna.
    Restricciones: La entrada tiene que ser un diccionario. 
    """
    print("----------------------------------------------------")
    for jugador in (listadejugadores):
        print("| ",end="")
        print(listadejugadores[jugador]["nombre"],": ",listadejugadores[jugador]["puntuacion"])
    print("----------------------------------------------------")

def mayorPuntuacion(listadejugadores):
	mayorPuntuacion = {"nombre":"","puntuacion":0}
	mayoresPuntuaciones = []
	for jugador,puntuacion in listadejugadores.items():
		if listadejugadores[jugador]["puntuacion"] > mayorPuntuacion["puntuacion"]:
			mayorPuntuacion["nombre"] = listadejugadores[jugador]["nombre"]
			mayorPuntuacion["puntuacion"] = listadejugadores[jugador]["puntuacion"]

	for jugador, puntuacion in listadejugadores.items():
		if listadejugadores[jugador]["puntuacion"] == mayorPuntuacion["puntuacion"]:
			mayoresPuntuaciones.append(listadejugadores[jugador]["nombre"]) 

	if len(mayoresPuntuaciones) > 1:
		print("Hubo un empate entre: \n",mayoresPuntuaciones)
	else:
		print(mayorPuntuacion["nombre"],"es el ganador")

def abrirPreguntas():
    with open("prueba.json","r", encoding="utf-8") as json_file:
        preguntas = json.load(json_file)
    print("-" * 100)
    return preguntas

def main():
	limpiarPantalla()
	mensajeBienvenida()
	listaJugadores = cantidadJugadores()
	mostrarPuntuacion(listaJugadores)
	rondas = 3
	listaPreguntas = abrirPreguntas()
	listaRepetidas = []
	preguntas = []
	respuesta = ""

	for ronda in range(rondas):
	
		while len(preguntas) < 5:
			pregunta = random.choice(list(listaPreguntas))
			if pregunta not in listaRepetidas:
				preguntas.append(pregunta)
				listaRepetidas.append(pregunta)
	
		for pregunta in preguntas:
			print(listaPreguntas[pregunta]["texto"])
		
			for opciones,valores in listaPreguntas[pregunta]["opciones"].items():
				print(opciones,": ",valores,"\n")
		
			for jugador in listaJugadores:
				respuesta = ""

				while respuesta not in ["a","b","c","d"]:
					respuesta = input(listaJugadores[jugador]["nombre"] + ": Ingrese su respuesta: ").lower()

				if respuesta == listaPreguntas[pregunta]["correcta"]:
					listaJugadores[jugador]["puntuacion"] += 1
		
			print("Respuesta correcta: " + listaPreguntas[pregunta]["correcta"])

		preguntas = []
		mostrarPuntuacion(listaJugadores)		   
	mayorPuntuacion(listaJugadores)

	while respuesta not in ["S","N"]:
		respuesta = input("Quiere jugar de nuevo, responda con S o N: ")
	
	if respuesta == "S":
		main()
	else:
		print("Fin del juego")

main()