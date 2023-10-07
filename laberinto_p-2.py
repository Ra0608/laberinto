
#while True:
 # k = readkey()
 # if k == "a":
    # do stuff
 # if k == key.DOWN:
    # do stuff
 # if k == key.ENTER:
   # break
from readchar import readkey, key
# se importa las librerias a usar
while True:
    print("toca una tecal: ")
#se le pide al usuario que oprima una letra
    letra=readkey()
    print(letra)
    if letra == key.UP:
    # presione UP para el juego
        print("termina el juego ")
    
        break
    