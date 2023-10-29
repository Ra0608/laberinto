from readchar import readkey,key
import os


def cambiar_mapa(laberinto):
    # Divide el mapa en filas y convierte cada fila en una lista de caracteres
    return [list(fila) for fila in laberinto.split('\n')]

def borrar_linea():
    # Limpia la pantalla en la consola 
    os.system('cls' if os.name == 'nt' else 'clear')
#se le pide al jugador  que oprima una letra
def imprimir_mapa(mapa):
 
    # Muestra la matriz en la consola
    for fila in mapa:
        print(''.join(fila))

def main_loop(mapa, posicion_inicial,posicion_final):
    px, py = posicion_inicial # Inicializa la posición del jugador en la posición de inicio
    
    while (px, py) != posicion_final:
        borrar_linea()
        mapa[px][py] = 'P'  # Coloca el caracter 'P' como si fuese el jugador 
        imprimir_mapa(mapa)
        mapa[px][py] = '.'
          # indica por donde puede ir el jugador '.'
                   
        tecla=readkey()#sirve para la lectura por teclado de cada movimiento
        if tecla == key.UP and px > 0 and mapa[px - 1][py] != '#':
            px -= 1
        elif tecla == key.DOWN and px < len(mapa) - 1 and mapa[px + 1][py] != '#':
            px += 1
        elif tecla == key.LEFT and py > 0 and mapa[px][py - 1] != '#':
            py -= 1
        elif tecla == key.RIGHT and py < len(mapa[0]) - 1 and mapa[px][py + 1] != '#':
            py += 1


laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

# Cambia el mapa en una matriz 
mapa = cambiar_mapa(laberinto)

# idica inicial y final
posicion_inicial = (0, 0)
posicion_final = (len(mapa) - 1, len(mapa[0]) - 1)
# Inicia el bucle principal
main_loop(mapa, posicion_inicial, posicion_final)
#muestra el mapa posicion inicial yla final 
print("felicidades jugador saliste del laberinto")
#al salir del laberinto se felicita al jugador 

