#----------- Proyecto 0 - Michael Araya Murcia - Jose Julian Araya Castillo -------
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
	for key in (listadejugadores):
		print(listadejugadores[key])

def abrirPreguntas():
	archivo = open("prueba.json","r")
	for linea in archivo.readlines():
		print(linea)
	archivo.close()


def main():
	mensajeBienvenida()
	lista = cantidadJugadores()
	mostrarPuntuacion(lista)

main()