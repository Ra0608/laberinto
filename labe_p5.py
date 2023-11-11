"""
PROYECTO INTEGRADO PARTE 5
Almacenando mapas en archivos
En lugar de almacenar el mapa en el mismo código, podemos guardarlo en 
archivos con sus posiciones de inicio y fin y las dimensiones del mapa en la primera 
línea del archivo, de esta manera los componentes de la aplicación estarán separados y 
podremos mejorar la experiencia del juego.

Crear una nueva clase JuegoArchivo la cual hereda de Juego,
Reescribir el constructor para leer un archivo al azar de una 
carpeta que contenga los mapas cada vez que se instancia el juego.
Para listar los archivos de un directorio usar os.listdir(path) , 
esto devolverá una lista con el nombre los archivos en ese directorio
Para elegir un elemento aleatorio de una lista usar random.choice(lista).
Note que para poder leer el archivo tenemos que componer el path, una forma 
de hacerlo es path_completo = f"{path_a_mapas}/{nombre_archivo}"
Crear un método que lea los datos de estos archivos de mapa y devuelva una cadena 
que tenga concatenada todas las filas leídas del mapa y las coordenadas de inicio y fin.
Al final de la lectura antes de retornar usar cadena.strip() para eliminar caracteres en blanco residuales.
"""
import os
from readchar import readkey,key
from pydantic import BaseModel
import random
class NotfileError(Exception):
     pass
class Juego(BaseModel):
    mapa:list| None
    laberinto : str | None
    posicion_inicial : tuple| None
    posicion_final: tuple| None       
    
    def cambiar_mapa(self,laberinto):
        self.mapa = [list(fila)for fila in self.laberinto.split('\n')]
     

    def borrar_linea(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def imprimir_mapa(self,mapa):    
        for fila in self.mapa:
          print(''.join(fila))

    def main_loop(self,mapa, posicion_inicial,posicion_final):
        px, py = posicion_inicial 
    
        while (px, py) != posicion_final:
            self.borrar_linea()
            mapa[px][py] = 'P'  
            self.imprimir_mapa(mapa)
            self.mapa[px][py] = '.' 
                
            tecla=readkey()
            
            if tecla == key.UP and px > 0 and self.mapa[px - 1][py] != '#':
                px -= 1
            elif tecla == key.DOWN and px < len(self.mapa) - 1 and self.mapa[px + 1][py] != '#':
                px += 1
            elif tecla == key.LEFT and py > 0 and self.mapa[px][py - 1] != '#':
                py -= 1
            elif tecla == key.RIGHT and py < len(self.mapa[0]) - 1 and self.mapa[px][py + 1] != '#':
                py += 1
        print("felicidades jugador saliste del laberinto")
    
class JuegoArchivo():
    def __init__(self):
        laberinto = self.leer_archivo()
        
        self.juego =Juego(posicion_inicial=(0,0),laberinto=laberinto,mapa=None,posicion_final = None)
        
    def leer_archivo(self)-> str:
        path = r"c:\Users\57321\Desktop\mapa\mapa"
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
        if os.path.exists(path):
            mapa = os.listdir(path)
            laberinto = list()
            if len(mapa) > 0:
                mapa = random.choice(mapa)
                with open(path+'/'+mapa,"r") as archivo:
                    laberinto = archivo.read()
            else:
                raise NotfileError (" se cargara el mapa por defecto")
        return laberinto.strip()
    
    def iniciar_el_juego(self):
        self.juego.cambiar_mapa(self.juego.laberinto)
        self.juego.main_loop(self.juego.mapa,self.juego.posicion_inicial,posicion_final=(len(self.juego.mapa) - 1, len(self.juego.mapa[0]) - 1))

Jugar =JuegoArchivo()
Jugar.iniciar_el_juego()