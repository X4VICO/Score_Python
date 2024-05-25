# SCRIPT EJECUTABLE
from scorelib import Score # importamos librería donde se encuentran las funciones
import sys # importamos "sys" para poder leer los parámetros introducidos

# ________________________ argumentos ________________________
# $ python score_this.py <puntuación> <iniciales> [archivo]
#              [0]           [1]          [2]        [3]
# ____________________________________________________________

# ___________________ verificación de ejecución ___________________
if len(sys.argv) < 3: # comprobamos que se introduzcan como mínimo 2 parámetros
    print("Uso: $ python score_this.py <puntuación> <iniciales> [archivo]") # si no se cumplen las condiciones necesarias, mostramos cuál sería la ejecución correcta del script
    sys.exit(1) # seguidamente salimos del script con un código de salida 1, esto sirve para saber que se sale por algún error

# ___________________ verificación de parámetros ___________________
# ----- verificación puntuación -----
try: # hacemos uso del try para asegurarnos de que la puntuación introducida solo consta de números
    points = int(sys.argv[1]) # guardamos los valores del argumento [1] en la variable "points"
except ValueError: # si se introduce algún carácter que no sea número...
    print("Error al registrar puntos. Deben ser números enteros.") # ... informamos del error...
    sys.exit(1) # ... seguidamente salimos del script con un código de salida 1

# ----- verificación nombre -----
name = sys.argv[2] # guardamos los valores del argumento [2] en la variable "name"
if len(name) != 3: # si no se introduce un nombre con una longitud de 3 caracteres alfanuméricos...
    print("Error al registrar créditos. Deben ser 3 caracteres.") # ... informamos del error...
    sys.exit(1) # ... seguidamente salimos del script con un código de salida 1

# ----- verificación archivo -----
# solo se guardará en "scorefile" el valor del argumento [3] si la longitud de argumentos es mayor a 3... 
scorefile = sys.argv[3] if len(sys.argv) > 3 else "score.txt" # ... de no ser el caso, se guardará por defecto como "score.txt"

# ___________________ añadir puntuación haciendo uso de "scorelib" ___________________
score = Score(scorefile) # creamos una instancia "Score" con archivo "scorefile"
score.add_score(points, name, scorefile) # pasamos los valores obtenidos a la función "add_score" que hay en la instancia "Score"
