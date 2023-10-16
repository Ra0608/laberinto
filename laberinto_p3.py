
"""""
Proyecto integrador parte 3
Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:
Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, 
borrar la terminal y e imprimir el nuevo número hasta el número 50.
La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.
Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción:
os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os
"""
import os
from readchar import readkey, key
def borrar_linea():
# definir una variable para la fusion os
     os.system('cls' if os.name=='nt' else 'clear')
     
def sumar_numero(nuevo_numero):
# se define variable para el nuevo numero
     print(nuevo_numero)
numeros=0
print("Biembenido jugador  presiona la tecla 'n' para iniciar el juego: ")
while True:
     letra=readkey()
     if letra =='n':
#se define la tecla n para iniciar el bucle          
          borrar_linea()
 # por cada vez que presione la tecla n borrara el numero anterior          
          sumar_numero(numeros)
          numeros=numeros+1
          if numeros==50+1:
               break
print("genial llegaste a 50 'fin del juego' ")
print("continuara.......")
               
     
        
      
      
             