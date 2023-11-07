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
